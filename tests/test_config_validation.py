import subprocess
import sys

def test_malformed_yaml(tmp_path):
    bad_yaml = """
    log_sources:
      - path: sample_logs/app.log
        options:
          summary_only: true
          export_path: output/summary.json
      - path: sample_logs/other.log
    this-is-bad-indentation
    """
    config_path = tmp_path / "bad.yaml"
    config_path.write_text(bad_yaml)

    result = subprocess.run(
        [sys.executable, "sherlock_logs.log_parser", "--config", str(config_path)],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode != 0
    assert "YAML parsing error" in result.stderr or "YAML parsing error" in result.stdout

def test_non_dict_yaml(tmp_path):
    not_a_dict_yaml = """
    - just
    - a
    - list
    """
    config_path = tmp_path / "not_dict.yaml"
    config_path.write_text(not_a_dict_yaml)

    result = subprocess.run(
        [sys.executable, "sherlock_logs.log_parser", "--config", str(config_path)],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode != 0
    assert "YAML parsing error" in result.stderr or "YAML parsing error" in result.stdout

def test_sys_exit_on_bad_yaml(tmp_path):
    broken_yaml = "::: this is not even YAML :::"
    config_path = tmp_path / "broken.yaml"
    config_path.write_text(broken_yaml)

    result = subprocess.run(
        [sys.executable, "sherlock_logs.log_parser", "--config", str(config_path)],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode != 0
    assert "YAML parsing error" in result.stderr or "YAML parsing error" in result.stdout
