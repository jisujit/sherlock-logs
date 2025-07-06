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

def main():
    parser = argparse.ArgumentParser(description="Sherlock Logs - Simple Log Reader")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the log file to read')
    args = parser.parse_args()

    read_log_file(args.file)

if __name__ == "__main__":
    main()
