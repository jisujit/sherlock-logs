# 🕵️‍♂️ sherlock-logs

![Python](https://img.shields.io/badge/python-3.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Last Commit](https://img.shields.io/github/last-commit/jisujit/sherlock-logs)
![Open Issues](https://img.shields.io/github/issues/jisujit/sherlock-logs)
![CI: Python Tests](https://github.com/jisujit/sherlock-logs/actions/workflows/python-tests.yml/badge.svg)

**sherlock-logs** is a powerful Python-based CLI tool that helps developers, DevOps engineers, and sysadmins analyze log files quickly and efficiently. It highlights errors, warnings, and status entries using styled output, and provides summaries and export options.

---
📌 Current Features reflect version: [v0.1.1](https://github.com/jisujit/sherlock-logs/releases/tag/v0.1.1)

## ✅ Features

- 🎨 Highlighted output using the [`rich`](https://github.com/Textualize/rich) library
  - `❌ ERROR / FATAL / FAILED` lines in red
  - `⚠️ WARNING / WARN` lines in yellow
  - `✅ OK / CHANGED / SUCCESS` lines in green
- 📊 Summary report per log file
- 🗂 Supports single log files and entire folders of `.log` files
- 🔍 Optional keyword filtering (e.g. `--filter ssh`)
- 📝 Export summary to `.json` or `.csv` (via `--export`)
- 💡 `--summary-only` mode to skip full log output
- 🧪 Unit testing support with `pytest`

---

## 🛠️ Setup Instructions

### Step 1: Clone this repository
```bash
git clone https://github.com/jisujit/sherlock-logs.git
cd sherlock-logs
```

### Step 2: Create and activate a virtual environment
```powershell
python -m venv venv-logAnalyzer
.\venv-logAnalyzer\Scripts\Activate.ps1
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Tool

### 🔹 Parse a single file
```bash
python log_parser.py --file sample_logs/ansible_sample.log
```

### 🔹 Summary-only mode
```bash
python log_parser.py --file sample_logs/ansible_sample.log --summary-only
```

### 🔹 Export to JSON or CSV
```bash
python log_parser.py --folder sample_logs/ --summary-only --export all_logs.json
python log_parser.py --folder sample_logs/ --summary-only --export all_logs.csv
```

### 🔹 Filter lines by keyword
```bash
python log_parser.py --file sample_logs/syslog_sample.log --filter ssh
```

---

## 🧪 Run Unit Tests

### 🔹 Enable pytest in VS Code (optional)
- Go to: `Settings > Python > Testing`
- Enable `pytest` and point to your virtual environment if needed

### 🔹 Run tests from terminal
```bash
pytest test_log_parser.py
```

---

## 📁 Folder Structure

```text
sherlock-logs/
├── sample_logs/             # Sample .log files
├── test_log_parser.py       # Pytest-based unit tests
├── requirements.txt         # Installed dependencies
├── .gitignore
├── README.md
├── tools/                   # Setup helper scripts
│   ├── setup-windows.ps1
│   └── setup-macos.sh
├── log_parser.py            # Main CLI tool
└── venv-logAnalyzer/        # Virtual environment (ignored by Git)
```

---

## 🔧 Optional: Use Setup Scripts

### 🪟 Windows
```powershell
.	.\tools\setup-windows.ps1
```

Then activate manually:
```powershell
.\venv-logAnalyzer\Scripts\Activate.ps1
```

---

### 🍎 macOS / 🐧 Linux
```bash
chmod +x tools/setup-macos.sh
./tools/setup-macos.sh
source venv-logAnalyzer/bin/activate
```

---

## 👤 Author

**Sujit Gangadharan**
📫 GitHub: [github.com/jisujit](https://github.com/jisujit)

---

## 📄 License

Distributed under the [MIT License](LICENSE).
Use it freely — just keep the credits. 🚀
