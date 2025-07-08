"""
log_parser.py

A simple log analysis tool that scans a log file and highlights
lines containing ERROR and WARNING messages using the rich library.

Author: Sujit Gangadharan
GitHub: https://github.com/jisujit
Created: 2025-07-05
License: MIT (see LICENSE file for details)
"""

import argparse
import os
import sys
import json
import csv
from typing import Dict
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

def read_log_file(file_path: str, summary_only: bool = False, filter_keyword: str = None) -> Dict[str, int]:
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

            # Apply keyword filter if provided
            if filter_keyword and filter_keyword.lower() not in line.lower():
                continue

            # Count types of log entries
            lower = line.lower()
            if any(w in lower for w in ["fatal", "failed", "error"]):
                error_count += 1
            elif any(w in lower for w in ["warning", "warn"]):
                warning_count += 1
            elif any(w in lower for w in ["ok", "changed", "success"]):
                ok_count += 1

            # Only print line if not in summary-only mode
            if not summary_only:
                styled_line = highlight_line(line)
                console.print(styled_line)

    # 🧾 Summary section
    console.print("\n[bold cyan]📊 Summary:[/]")
    console.print(f"  ❌ Errors/Fatals : [bold red]{error_count}[/]")
    console.print(f"  ⚠️  Warnings      : [bold yellow]{warning_count}[/]")
    console.print(f"  ✅ OK/Changed    : [bold green]{ok_count}[/]\n")

    # Return a dictionary of summary counts.
    # This enables writing the results to JSON or CSV if --export is used.
    return {
        "errors": error_count,
        "warnings": warning_count,
        "ok": ok_count
    }

def process_folder(folder_path: str, summary_only: bool = False, export_path: str = None, filter_keyword: str = None) -> None:
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

        # 🟩 Capture the summary returned from read_log_file()
        summary = read_log_file(full_path, summary_only=summary_only, filter_keyword=filter_keyword)

        # 🟩 Write it to file if export path is set
        if export_path:
            write_summary(full_path, summary, export_path)

def write_summary(file_path: str, summary: dict, export_path: str) -> None:
    """
    Write the summary to a .json or .csv file based on extension.
    """
    export_path = os.path.abspath(export_path)
    base_name = os.path.basename(file_path)

    # For multiple files, include filename in record
    summary_data = { "file": base_name, **summary }

    if export_path.endswith(".json"):
        existing = []
        if os.path.isfile(export_path):
            with open(export_path, "r") as f:
                try:
                    existing = json.load(f)
                except json.JSONDecodeError:
                    pass
        existing.append(summary_data)
        with open(export_path, "w") as f:
            json.dump(existing, f, indent=2)

    elif export_path.endswith(".csv"):
        write_header = not os.path.isfile(export_path)
        with open(export_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=summary_data.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(summary_data)

    else:
        console.print(f"[red]❌ Unsupported export format: {export_path}[/]")

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
    parser.add_argument('--export', '-e', type=str, help='Path to export summary (supports .json or .csv)')
    parser.add_argument('--filter', type=str, help='Only show lines containing this keyword (case-insensitive)')

    args = parser.parse_args()

    if args.file:
        # 🟡 1. Capture summary returned from file parser
        summary = read_log_file(args.file, summary_only=args.summary_only, filter_keyword=args.filter)

        # 🟡 2. If user provided --export, write the summary to file
        if args.export:
            write_summary(args.file, summary, args.export)

    elif args.folder:
        # 🟡 3. Pass export path to folder processor (you'll update process_folder to accept this)
        process_folder(args.folder, summary_only=args.summary_only, export_path=args.export, filter_keyword=args.filter)

if __name__ == "__main__":
    main()
