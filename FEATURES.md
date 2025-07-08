
# 📦 sherlock-logs – Features Overview

> 📦 Feature Summary for Release: v0.1.1
> 🗓️ Last Updated: 2025-07-08

## 🧠 Core Functionality

- **Color-coded highlighting** of log lines using [`rich`](https://github.com/Textualize/rich):
  - `❌ ERROR / FATAL / FAILED` → Red
  - `⚠️ WARNING / WARN` → Yellow
  - `✅ OK / CHANGED / SUCCESS` → Green
- **Command-line support** with useful flags:
  - `--summary-only`: Show only error/warning summary
  - `--output`: Save output to a file (`.txt` or `.json`)
  - `--filter`: Filter by keywords (e.g., `--filter ssh`)
- **Batch processing**: Analyze both single log files and folders
- **Modular code**: Easy to extend for future formats (JSON logs, structured input)
- **Planned support** for interactive and exportable reporting (see roadmap)

## 🧪 Testing & Quality

- `pytest` test suite under `tests/`
  - Includes unit tests for `highlight_line()` and CLI behaviors
  - Relies on sample logs (`sample_logs/*.log`) for consistent regression testing

## 🤖 GitHub Actions: Continuous Integration (CI)

- GitHub Actions workflow `python-tests.yml`
  - Automatically runs tests on every push or PR to `main`
  - Test badge displayed in `README.md`
  - Ensures stable, test-passing code at all times

## 📄 Documentation & Dev Readiness

- `README.md`: Quickstart, usage, badges, and examples
- `CONTRIBUTING.md`: Clear guidelines for contributors
- `CHANGELOG.md`: Tracks version history with semantic versioning
- `LICENSE`: MIT license for open-source sharing

## 🚀 Project Planning

- Defined milestones:
  - `v0.2.0`: Config-driven execution
  - `v0.3.0`: JSON log parsing
  - `v0.4.0`: Regex & datetime filtering
  - `v0.5.0`: Interactive TUI (Text UI)
  - `v0.6.0`: Report exports (HTML, PDF, Markdown)
- GitHub Issues linked to milestones for tracking

## 🔁 Development Workflow

- Uses feature branches and Pull Requests to `main`
- All changes tested via CI before merge
- Follows semantic versioning:
  - `v0.1.0`: Base feature release
  - `v0.1.1`: Docs, tests, CI automation