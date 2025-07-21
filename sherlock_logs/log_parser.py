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
import yaml
from rich.console import Console
from rich.text import Text
from sherlock_logs.config_loader import load_config, ConfigLoadError

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
        console.print(f"❌ Error: File not found -> {file_path}")
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
        console.print(f"❌ Error: Folder not found -> {folder_path}")
        sys.exit(1)

    log_files = [f for f in os.listdir(folder_path) if f.endswith(".log")]
    if not log_files:
        console.print(f"⚠️ No .log files found in folder: {folder_path}")
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
            with open(export_path, "r", encoding="utf-8") as f:
                try:
                    existing = json.load(f)
                except json.JSONDecodeError:
                    pass
        existing.append(summary_data)
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2)

    elif export_path.endswith(".csv"):
        write_header = not os.path.isfile(export_path)
        with open(export_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=summary_data.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(summary_data)

    else:
        console.print(f"[red]❌ Unsupported export format: {export_path}[/]")

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Sherlock Logs - Log Parser with CLI Support")
    # Temporarily allow all args to be optional (we'll validate later)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--file', '-f', type=str, help='Path to a single log file')
    group.add_argument('--folder', '-d', type=str, help='Path to a folder containing .log files')
    parser.add_argument('--summary-only', '-s', action='store_true', help='Only print summary, skip full log output')
    parser.add_argument('--export', '-e', type=str, help='Path to export summary (supports .json or .csv)')
    parser.add_argument('--filter', type=str, help='Only show lines containing this keyword (case-insensitive)')
    parser.add_argument('--config', type=str, help='Path to a config.yaml file to override CLI options')

    args = parser.parse_args()

    # Manual validation: either --config or one of --file/--folder must be present
    if not (args.file or args.folder or args.config):
        parser.error("At least one of --file, --folder, or --config must be specified.")

    return args


def run_from_file(file_path: str, summary_only: bool, export_path: str, filter_keyword: str) -> None:
    """
    Process a single log file using the given parameters.
    Outputs styled log lines and optionally exports a summary.
    """
    summary = read_log_file(file_path, summary_only=summary_only, filter_keyword=filter_keyword)
    if export_path:
        write_summary(file_path, summary, export_path)


def run_from_folder(folder_path: str, summary_only: bool, export_path: str, filter_keyword: str) -> None:
    """
    Process all .log files in a folder using the given parameters.
    Outputs styled log lines and optionally exports a summary per file.
    """
    process_folder(folder_path, summary_only=summary_only, export_path=export_path, filter_keyword=filter_keyword)

def run_from_config(config_path: str) -> None:
    """
    Load configuration from a YAML file and process all specified log sources.
    Config options can override CLI arguments.
    """
    try:
        config = load_config(config_path)
    except ConfigLoadError as e:
        console.print(f"[bold red]❌ YAML parsing error:[/] {e}")
        sys.exit(1)

    log_sources = config.get("log_sources", [])
    options = config.get("options", {})

    summary_only = options.get("summary_only", False)
    filter_keyword = options.get("filter", None)
    export_path = options.get("export_path", None)

    for source in log_sources:
        path = source.get("path")
        if not path:
            continue

        if os.path.isdir(path):
            run_from_folder(path, summary_only, export_path, filter_keyword)
        elif os.path.isfile(path):
            run_from_file(path, summary_only, export_path, filter_keyword)
        else:
            console.print(f"[red]⚠️ Invalid path in config: {path}[/]")

def main() -> None:
    """
    Entry point of the CLI tool.
    Supports file, folder, or config-based log parsing.
    """
    args = parse_arguments()

    if args.config:
        run_from_config(args.config)
    elif args.file:
        run_from_file(args.file, args.summary_only, args.export, args.filter)
    elif args.folder:
        run_from_folder(args.folder, args.summary_only, args.export, args.filter)


if __name__ == "__main__":
    main()
