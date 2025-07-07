# 📜 Changelog

All notable changes to this project will be documented in this file.

The format follows [Semantic Versioning](https://semver.org/).

---

## [v0.1.2] - 2025-07-07
### Added
- `CONTRIBUTING.md` with clear contribution and development workflow
- Initialized `CHANGELOG.md` to track versioned progress

### Notes
- No functional or code changes were introduced in this release

---

## [v0.1.1] - 2025-07-07
### Added
- Project badges to `README.md` (Python version, license, last commit, open issues)
- Minor cleanup and formatting improvements in documentation

---

## [v0.1.0] - 2025-07-06
### Initial Release
- Highlights log lines containing `ERROR` and `WARNING` using the `rich` library
- `--summary-only` flag to display a condensed list of matching log lines
- Option to save results in `.txt` or `.json` format using `--output`
- Initial test for `highlight_line` using `pytest`
- Clean project structure with `requirements.txt` and detailed `README.md`
- Easy to set up with `venv` and install dependencies
- Project scaffold designed for extensibility (future JSON log support, TUI, etc.)