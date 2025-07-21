"""
Integration test for config-driven execution of log_parser.
"""

# --------------------------------------------------------------------
# Author        : Sujit Gangadharan
# Created       : 2025-07-14
# Email         : gsujit@gmail.com
# License       : MIT
# Description   : Tests that log_parser correctly processes config.yaml.
# --------------------------------------------------------------------

import subprocess
import json
import yaml

def test_config_driven_execution(tmp_path):
    """
    Test that the log_parser runs correctly with a config file.
    Verifies that a temp summary.json is created and contains expected fields.
    """

    # 1️⃣ Prepare temporary output path
    export_path = tmp_path / "summary.json"

    # 2️⃣ Clone original config.yaml and update export_path
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["options"]["export_path"] = str(export_path)

    # 3️⃣ Write a temp config.yaml in tmp_path
    temp_config_path = tmp_path / "temp_config.yaml"
    with open(temp_config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f)

    # 4️⃣ Run the parser using the temp config
    result = subprocess.run(
        [sys.executable, "-m", "sherlock_logs.log_parser", "--config", str(temp_config_path)],
        capture_output=True,
        text=True,
        check=True
    )

    assert result.returncode == 0, f"Script failed: {result.stderr}"

    # 5️⃣ Check that summary.json exists and contains valid data
    assert export_path.exists(), "summary.json was not created"

    with open(export_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list), "summary.json should be a list"
        assert len(data) >= 1, "summary.json should contain at least one result"
        for entry in data:
            assert "file" in entry
            assert "errors" in entry
            assert "warnings" in entry
            assert "ok" in entry
