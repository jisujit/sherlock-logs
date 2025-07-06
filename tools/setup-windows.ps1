# tools/setup.ps1
<#
Author: Sujit Gangadharan
GitHub: https://github.com/jisujit
Created: 2025-07-05
Description: PowerShell script to set up Python virtual environment and install project dependencies.
#>
Write-Host "🚀 Starting setup process..."

# Define the name of the virtual environment
$envName = "venv-logAnalyzer"

# Check if Python is installed
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "❌ Error: Python is not installed or not in PATH. Please install Python 3 and try again."
    exit 1
}

# Check if virtual environment already exists
if (Test-Path ".\$envName") {
    Write-Host "⚠️  Virtual environment '$envName' already exists. Skipping creation."
}
else {
    # Step 1: Create virtual environment
    Write-Host "🔧 Creating virtual environment: $envName"
    python -m venv $envName
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Error: Failed to create virtual environment '$envName'. Please check your Python installation."
        exit 1
    }
}
# Step 1: Create virtual environment
Write-Host "🔧 Creating virtual environment: $envName"
python -m venv $envName

# Step 2: Prompt for manual activation
Write-Host "`n👉 IMPORTANT: Please activate the virtual environment manually:"
Write-Host ".\$envName\Scripts\Activate.ps1`n"

# Step 3: Upgrade pip
Write-Host "⬆️  Upgrading pip..."
& ".\$envName\Scripts\python.exe" -m pip install --upgrade pip

# Step 4: Install dependencies if requirements.txt exists
if (Test-Path ".\requirements.txt") {
    Write-Host "📦 Installing dependencies from requirements.txt..."
    & ".\$envName\Scripts\python.exe" -m pip install -r requirements.txt
} else {
    Write-Host "⚠️  No requirements.txt found. Skipping dependency installation."
}

# Step 5: Freeze to requirements.txt (with backup if file exists)
if (Test-Path ".\requirements.txt") {
    $timestamp = Get-Date -Format "yyyyMMddHHmmss"
    $backupFile = ".\requirements.txt.backup.$timestamp"
    Write-Host "🗂️  Backing up existing requirements.txt to $backupFile before freezing."
    Copy-Item ".\requirements.txt" $backupFile
}
Write-Host "📄 Freezing environment to requirements.txt..."
& ".\$envName\Scripts\python.exe" -m pip freeze > requirements.txt

Write-Host "`n✅ Setup complete. Don't forget to activate the virtual environment before running the project."
