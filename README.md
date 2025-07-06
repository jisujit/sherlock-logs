
# 🕵️‍♂️ sherlock-logs
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
├── venv-logAnalyzer/ # Virtual environment (ignored by Git)
├── requirements.txt # Installed dependencies
├── .gitignore # Ignored files and folders
├── README.md # Project overview
└── log_parser.py # Main script (to be created)
```

### 👤 Author
Sujit Gangadharan
GitHub: [github.com/jisujit](https://github.com/jisujit)