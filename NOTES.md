# Project Notes: sherlock-logs

## README Development
- Used [Dillinger.io](https://dillinger.io/) and [StackEdit.io](https://stackedit.io/) for Markdown editing.
- Final version of `README.md` was created using **Dillinger.io**.

## Setup Notes
- PowerShell setup script: `tools/setup-windows.ps1`
- macOS/Linux script: `tools/setup-macos.sh`

## TODOs
- Add support for custom log formats
- Implement log_parser.py with argparse
- Implement .commitlintrc

## Resources
- https://rich.readthedocs.io/

# Commitlint & .commitlintrc Setup Notes

## 📌 What is Commitlint?

**Commitlint** is a tool that checks if your Git commit messages meet a defined convention (like [Conventional Commits](https://www.conventionalcommits.org/)).

---

## 📁 What is `.commitlintrc`?

This config file tells Commitlint what rules to enforce.

### ✅ Example `.commitlintrc.json`

```json
{
  "extends": ["@commitlint/config-conventional"],
  "rules": {
    "type-enum": [
      2,
      "always",
      ["feat", "fix", "docs", "style", "refactor", "perf", "test", "chore"]
    ],
    "subject-case": [2, "never", ["start-case", "pascal-case"]],
    "scope-empty": [1, "never"]
  }
}
```

---

## 🛠 How to Set Up Commitlint (Optional)

### Step 1: Initialize Node Project

```bash
npm init -y
```

### Step 2: Install Dependencies

```bash
npm install --save-dev @commitlint/{cli,config-conventional} husky
```

### Step 3: Enable Husky Git Hooks

```bash
npx husky install
```

### Step 4: Add a Commit Message Hook

```bash
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

This will check commit messages before they are saved.

---

## 💡 Why Use This?

- Enforces clean commit history
- Prevents vague messages like "fix stuff"
- Helps automation, changelogs, and team collaboration

---

## 🔚 Do I Need It?

For solo projects: Optional
For team/shared projects: Highly recommended