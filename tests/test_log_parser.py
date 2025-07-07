"""
Unit tests for log_parser tool functions using pytest.
"""

# ------------------------------------------------------------------------------
# Author        : Sujit Gangadharan
# Created       : 2025-07-10
# Last Updated  : 2025-07-10
# Email         : gsujit@gmail.com
# License       : MIT
# Description   : Test suite for highlight_line() and other core utilities.
# ------------------------------------------------------------------------------

# Example usage:
#   pytest test_log_parser.py


from log_parser import highlight_line

def test_highlight_error():
    """Highlight line with error keyword."""
    line = "2025-07-06 10:30:15,123 ERROR: Something failed"
    styled = highlight_line(line)
    assert styled.style == "bold red"

def test_highlight_warning():
    """Highlight line with warning keyword."""
    line = "2025-07-06 10:30:15,123 WARNING: Low disk space"
    styled = highlight_line(line)
    assert styled.style == "yellow"

def test_highlight_ok():
    """Highlight line with success keyword."""
    line = "2025-07-06 10:30:15,123 TASK [changed]: Configuration applied"
    styled = highlight_line(line)
    assert styled.style == "green"

def test_highlight_default():
    """Highlight line with no keywords."""
    line = "2025-07-06 10:30:15,123 INFO: Starting up"
    styled = highlight_line(line)
    assert styled.style == "white"
