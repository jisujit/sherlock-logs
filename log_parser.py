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

def read_log_file(file_path: str) -> None:
    """
    Reads the specified log file and prints each line with
    styled output using Rich based on log severity levels.

    Args:
        file_path (str): Path to the log file to be read
    """
    if not os.path.isfile(file_path):
        print(f"❌ Error: File not found -> {file_path}")
        sys.exit(1)

    console.print(f"\n📄 [bold underline]Reading log file:[/] {file_path}\n")

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.strip():
                console.print(highlight_line(line))

def process_folder(folder_path: str) -> None:
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
        read_log_file(full_path)

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
    args = parser.parse_args()

    if args.file:
        read_log_file(args.file)
    elif args.folder:
        process_folder(args.folder)

if __name__ == "__main__":
    main()
