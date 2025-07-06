#!/bin/bash

# Author: Sujit Gangadharan
# GitHub: https://github.com/jisujit
# Created: 2025-07-05
# Description: Shell script to set up Python virtual environment and install project dependencies on macOS/Linux.

echo "🚀 Starting setup process..."

# Step 1: Define the virtual environment name
ENV_NAME="venv-logAnalyzer"

# Step 2: Create virtual environment
echo "🔧 Creating virtual environment: $ENV_NAME"
python3 -m venv "$ENV_NAME"

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

# Step 6: Freeze environment to requirements.txt
echo "📄 Freezing environment to requirements.txt..."
"$ENV_NAME/bin/python" -m pip freeze > requirements.txt

echo -e "\n✅ Setup complete. Don't forget to activate the virtual environment before running the project."
