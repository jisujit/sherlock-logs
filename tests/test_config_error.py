"""
Test case for handling an invalid config file in config-driven mode.
"""

# --------------------------------------------------------------------
# Author        : Sujit Gangadharan
# Created       : 2025-07-14
# Email         : gsujit@gmail.com
# License       : MIT
# Description   : Tests that the CLI properly handles a missing/invalid config.
# --------------------------------------------------------------------

import subprocess

def test_invalid_config_file():
    """
    Run the CLI tool with a non-existent config file and verify it fails gracefully.
    """
    result = subprocess.run(
        [sys.executable, "-m", "sherlock_logs.log_parser", "--config", str(config_path)],
        capture_output=True,
        text=True,
        check=False  # ✅ Explicitly allow subprocess to fail
    )

    assert result.returncode != 0, "Expected failure for invalid config file"
    assert "No such file or directory" in result.stderr or "❌" in result.stderr
