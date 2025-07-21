"""
Test handling of malformed YAML config in config-driven execution.
"""

# --------------------------------------------------------------------
# Author        : Sujit Gangadharan
# Created       : 2025-07-14
# Email         : gsujit@gmail.com
# License       : MIT
# Description   : This test verifies the tool exits gracefully when a malformed YAML config is passed.
# --------------------------------------------------------------------

import subprocess
import sys

def test_malformed_yaml(tmp_path):
    """
    Create a malformed config.yaml and run the tool to ensure
    it fails gracefully with a YAML parser error.
    """
    # 🔸 1. Create a malformed config file
    malformed_yaml = """
    log_sources:
      - path: sample_logs/ansible_sample.log
        options:
          summary_only: true
          export_path: output/summary.json
      - path: sample_logs/ansible_sample2.log
    this-is-bad-indentation
    """
    bad_config_path = tmp_path / "bad_config.yaml"
    bad_config_path.write_text(malformed_yaml)

    # 🔸 2. Run the parser with the bad config
    result = subprocess.run(
        [sys.executable, "sherlock_logs.log_parser", "--config", str(bad_config_path)],
        capture_output=True,
        text=True,
        check=False  # Allow the failure so we can test it
    )

    # 🔸 3. Assertions and graceful output
    print("\n🔍 Malformed YAML test executed")
    print("Return Code:", result.returncode)
    print("Standard Error Output:")
    print(result.stderr.strip())

    assert result.returncode != 0, "Expected failure due to malformed YAML"
    assert any(keyword in result.stderr.lower() for keyword in ["yaml", "scanner error", "could not parse"]), (
        "Expected YAML error message not found in stderr."
    )

    print("✅ Malformed YAML test passed — Parser failed gracefully.\n")
