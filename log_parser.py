import argparse
import os
import sys

def read_log_file(file_path):
    if not os.path.isfile(file_path):
        print(f"❌ Error: File not found -> {file_path}")
        sys.exit(1)

    print(f"\n📄 Reading log file: {file_path}\n")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.strip():  # Only print non-empty lines
                print(line.rstrip())

def main():
    parser = argparse.ArgumentParser(description="Sherlock Logs - Simple Log Reader")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the log file to read')
    args = parser.parse_args()

    read_log_file(args.file)

if __name__ == "__main__":
    main()
