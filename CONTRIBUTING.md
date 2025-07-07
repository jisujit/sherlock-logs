# Contributing to sherlock-logs

Thank you for your interest in contributing to `sherlock-logs`! Whether you're fixing a bug, improving documentation, or adding a new feature — your contributions are welcome.

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/sherlock-logs.git
   cd sherlock-logs
   ```
3. **Create a new branch** for your change:
   ```bash
   git checkout -b feature/my-feature-name
   ```

## 📋 Contributing Guidelines

- Follow existing code style and structure.
- Commit with clear, descriptive messages (e.g., `feat: add --config flag support`).
- Keep pull requests focused on a single change or feature.
- If you're fixing a bug, try to include a test or reproduction steps.

## 📂 Project Structure

- `log_scanner.py` – main CLI entry point
- `utils/` – helper functions (to be expanded)
- `tests/` – unit tests
- `README.md` – project documentation

## 🧪 Running Locally

Set up your virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Run the tool:

```bash
python log_scanner.py --file path/to/log.txt
```

Run tests:

```bash
pytest tests/
```

## 📢 Reporting Issues

If you find a bug or want to suggest a feature, please open an [Issue](https://github.com/jisujit/sherlock-logs/issues) with details and reproduction steps.

## 🙏 Thank You

Your time and contributions are greatly appreciated!
