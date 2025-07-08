""" Generic Test to read sample log files """

import os

def test_sample_log_reading():
    """
    Test that the sample Ansible log file exists and can be read correctly.

    - Verifies the file is accessible using a dynamic relative path
    - Prints total number of lines and the first 5 sample lines
    """
    sample_log_path = os.path.join(
        os.path.dirname(__file__),
        '..', 'sample_logs', 'ansible_sample.log'
    )
    sample_log_path = os.path.abspath(sample_log_path)

    with open(sample_log_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        print(f"Total lines: {len(lines)}")
        for line in lines[:5]:
            print(f"Sample line: {line}")
