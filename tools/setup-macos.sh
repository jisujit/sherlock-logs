#!/bin/bash

# Author: Sujit Gangadharan
# GitHub: https://github.com/jisujit
# Created: 2025-07-05
# Description: Shell script to set up Python virtual environment and install project dependencies on macOS/Linux.

echo "🚀 Starting setup process..."

# Step 1: Define the virtual environment name
ENV_NAME="venv-logAnalyzer"

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH. Please install Python 3 and try again."
    exit 1
fi

# Check if virtual environment already exists
if [ -d "$ENV_NAME" ]; then
    echo "⚠️  Virtual environment '$ENV_NAME' already exists. Skipping creation."
else
    # Step 2: Create virtual environment
    echo "🔧 Creating virtual environment: $ENV_NAME"
    python3 -m venv "$ENV_NAME"
    if [ $? -ne 0 ]; then
        echo "❌ Error: Failed to create virtual environment '$ENV_NAME'. Please check your Python installation."
        exit 1
    fi
fi

# Step 3: Prompt for manual activation
echo -e "\n👉 IMPORTANT: Please activate the virtual environment manually:"
echo "source $ENV_NAME/bin/activate"
echo

# Step 4: Upgrade pip
echo "⬆️  Upgrading pip..."
"$ENV_NAME/bin/python" -m pip install --upgrade pip

# Step 5: Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt..."
    "$ENV_NAME/bin/python" -m pip install -r requirements.txt
else
    echo "⚠️  No requirements.txt found. Skipping dependency installation."
fi

# Step 6: Freeze environment to requirements.txt (optional, with backup if file exists)
FREEZE=0
for arg in "$@"; do
    if [ "$arg" = "--freeze" ]; then
        FREEZE=1
    fi
    if [ "$arg" = "-f" ]; then
        FREEZE=1
    fi
    if [ "$arg" = "--no-freeze" ]; then
        FREEZE=0
    fi
    if [ "$arg" = "-n" ]; then
        FREEZE=0
    fi
done

if [ $FREEZE -eq 1 ]; then
    if [ -f "requirements.txt" ]; then
        BACKUP_FILE="requirements.txt.backup.$(date +%Y%m%d%H%M%S)"
        echo "🗂️  Backing up existing requirements.txt to $BACKUP_FILE before freezing."
        cp requirements.txt "$BACKUP_FILE"
    fi
    echo "📄 Freezing environment to requirements.txt..."
    "$ENV_NAME/bin/python" -m pip freeze > requirements.txt
else
    echo "ℹ️  Skipping pip freeze to requirements.txt. Use --freeze to enable."
fi

echo -e "\n✅ Setup complete. Don't forget to activate the virtual environment before running the project."
