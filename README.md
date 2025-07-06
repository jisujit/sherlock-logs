
# 🕵️‍♂️ sherlock-logs
![Python](https://img.shields.io/badge/python-3.11-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Last Commit](https://img.shields.io/github/last-commit/jisujit/sherlock-logs)

**sherlock-logs** is a Python tool to help developers and engineers quickly scan and highlight important entries in log files — especially errors and warnings.

## Features
- Highlights `ERROR` and `WARNING` lines in color
- Simple, readable output using the [`rich`](https://github.com/Textualize/rich) library
- Easy to extend for different log formats

## 🛠️ Setup Instructions

### Step 1: Clone this repository
```bash
git  clone  https://github.com/jisujit/sherlock-logs.git
cd  sherlock-logs
```

### Step  2:  Create  and  activate  a  virtual  environment
``` powershell
python  -m venv venv-logAnalyzer
.env-logAnalyzer\Scripts\Activate.ps1
```
### Step 3: Install dependencies
```bash
pip  install  -r  requirements.txt
```

### ▶️ Run the Tool
```bash
#Run the parser
python  log_parser.py
```

### 📁 Folder Structure

```text
sherlock-logs/
├── venv-logAnalyzer/       # Virtual environment (ignored by Git)
├── requirements.txt        # Installed dependencies
├── .gitignore              # Ignored files and folders
├── README.md               # Project overview
├── tools/                  # Utility setup scripts
│   ├── setup-windows.ps1   # Setup script for Windows
│   └── setup-macos.sh      # Setup script for macOS/Linux
└── log_parser.py           # Main script (to be created)
```

## 🔧 Optional: Setup Script
If you prefer automated setup, use the provided platform-specific script to create and configure your virtual environment:

### 🪟 Windows
``` powershell
# Run from the root of the project
.\tools\setup-windows.ps1
```

##### This script will:
- Create the venv-logAnalyzer virtual environment
- Prompt you to activate it manually
- Upgrade pip
- Install packages from requirements.txt (if present)
- Freeze installed packages back into requirements.txt

#### 💡 Manual activation required after script runs:
``` powershell
.\venv-logAnalyzer\Scripts\Activate.ps1
```
### 🍎 macOS / 🐧 Linux
``` bash
# Make script executable (first time only)
chmod +x tools/setup-macos.sh

# Then run
./tools/setup-macos.sh
```
This script performs the same steps as the Windows version.


#### 💡 Manual activation required after script runs:
``` bash
source venv-logAnalyzer/bin/activate
```
### 👤 Author
Sujit Gangadharan
GitHub: [github.com/jisujit](https://github.com/jisujit)

## 📄 License
Distributed under the [MIT License](LICENSE) — use it freely, just keep the credits. 🚀