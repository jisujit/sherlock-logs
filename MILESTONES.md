# 📌 sherlock-logs Milestones

This document outlines current and planned milestones for the `sherlock-logs` CLI tool.

---

## ✅ v0.1.0 – Initial Release

**Release Date:** [Insert Date]

### Features:
- 🔍 Command-line tool to parse `.log` files with colored output using `rich`
- 🎯 Highlights:
  - `ERROR`, `FATAL`, `FAILED` → 🔴 Red
  - `WARNING`, `WARN` → 🟡 Yellow
  - `OK`, `CHANGED`, `SUCCESS` → 🟢 Green
- 📊 Summary section with totals for:
  - Errors/Fatals
  - Warnings
  - OK/Changed
- 📁 Supports parsing:
  - A single log file (`--file`)
  - A folder of `.log` files (`--folder`)
- 🎛️ Additional Options:
  - `--summary-only` to show only summaries
  - `--filter` keyword-based line filtering
  - `--export` to save summary to `.json` or `.csv`
- 🧪 Unit tests started with `pytest`
- 🧰 Setup scripts for Windows/macOS
- 🗃️ Clean project structure with `README`, `requirements.txt`, and tool scripts

---

## 🚧 Planned Milestones

### 🔹 v0.2.0 – Config-Driven Execution
- ✅ Add support for `config.txt` or `.ini` file for defining:
  - Input paths
  - Summary-only flag
  - Filters
- ✅ Improve usability for non-CLI users

---

### 🔹 v0.3.0 – JSON Log File Parsing
- ✅ Parse `.json` log files
- ✅ Support both arrays and line-delimited JSON
- ✅ Allow user to define JSON fields for:
  - Message
  - Level (error/warn/info)
  - Timestamp (optional)

---

### 🔹 v0.4.0 – Enhanced Filtering
- ✅ Regex-based filters
- ✅ Combine multiple filters (e.g. include and exclude)
- ✅ Date/time range filtering

---

### 🔹 v0.5.0 – Interactive Terminal UI (TUI)
- ✅ Optional `--interactive` flag launches a TUI to:
  - Browse files
  - View colored logs
  - Search interactively
  - Navigate summaries

---

### 🔹 v0.6.0 – Advanced Reporting and Export
- ✅ Export formatted reports:
  - HTML
  - PDF
  - Markdown
- ✅ Use templates for customized output
- ✅ Useful for documentation, ticketing systems, and dashboards

---

🎯 **Have feature ideas or want to contribute?**
Open a [GitHub Issue](https://github.com/jisujit/sherlock-logs/issues) or submit a pull request!
