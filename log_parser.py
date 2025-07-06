import argparse
import os
import sys
from rich.console import Console
from rich.text import Text

console = Console()

def highlight_line(line: str) -> Text:
    """
    Analyze a single log line and apply color styling
    based on keywords like 'error', 'warning', 'ok', etc.

    Args:
        line (str): A single line from the log file

    Returns:
        Text: A Rich Text object with styling applied
    """
    lower_line = line.lower()

    if "fatal" in lower_line or "failed" in lower_line or "error" in lower_line:
        return Text(line.rstrip(), style="bold red")
    elif "warning" in lower_line or "warn" in lower_line:
        return Text(line.rstrip(), style="yellow")
    elif "ok" in lower_line or "changed" in lower_line or "success" in lower_line:
        return Text(line.rstrip(), style="green")
    else:
        return Text(line.rstrip(), style="white")

def read_log_file(file_path: str, summary_only: bool = False) -> None:
    """
    Reads a log file and prints each line with styling.
    Also collects and prints a summary of important keywords.
    """
    if not os.path.isfile(file_path):
        print(f"❌ Error: File not found -> {file_path}")
        sys.exit(1)

    error_count = 0
    warning_count = 0
    ok_count = 0

    console.print(f"\n📄 [bold underline]Reading log file:[/] {file_path}\n")

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if not line.strip():
                continue

            lower = line.lower()
            if any(w in lower for w in ["fatal", "failed", "error"]):
                error_count += 1
            elif any(w in lower for w in ["warning", "warn"]):
                warning_count += 1
            elif any(w in lower for w in ["ok", "changed", "success"]):
                ok_count += 1

            if not summary_only:
                styled_line = highlight_line(line)
                console.print(styled_line)

    # 🧾 Summary section
    console.print("\n[bold cyan]📊 Summary:[/]")
    console.print(f"  ❌ Errors/Fatals : [bold red]{error_count}[/]")
    console.print(f"  ⚠️  Warnings      : [bold yellow]{warning_count}[/]")
    console.print(f"  ✅ OK/Changed    : [bold green]{ok_count}[/]\n")

def process_folder(folder_path: str, summary_only: bool = False) -> None:
    """
    Process all `.log` files in the given folder and
    display their contents with styled output.
    """
    if not os.path.isdir(folder_path):
        print(f"❌ Error: Folder not found -> {folder_path}")
        sys.exit(1)

    log_files = [f for f in os.listdir(folder_path) if f.endswith(".log")]
    if not log_files:
        print(f"⚠️ No .log files found in folder: {folder_path}")
        return

    for log_file in log_files:
        full_path = os.path.join(folder_path, log_file)
        read_log_file(full_path, summary_only=summary_only)

def main() -> None:
    """
    Entry point of the CLI tool.
    Parses command-line arguments and determines
    whether to process a single file or a folder.
    """
    parser = argparse.ArgumentParser(description="Sherlock Logs - Log Parser with CLI Support")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', '-f', type=str, help='Path to a single log file')
    group.add_argument('--folder', '-d', type=str, help='Path to a folder containing .log files')
    parser.add_argument('--summary-only', '-s', action='store_true', help='Only print summary, skip full log output')
    args = parser.parse_args()

    if args.file:
        read_log_file(args.file, summary_only=args.summary_only)
    elif args.folder:
        process_folder(args.folder, summary_only=args.summary_only)

if __name__ == "__main__":
    main()
