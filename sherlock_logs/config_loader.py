"""
config_loader.py
Load and validate YAML config for sherlock-logs.

Author: Sujit Gangadharan
GitHub: https://github.com/jisujit
Created: 2025-07-13
License: MIT (see LICENSE file for details)
"""

import os
from typing import Dict, Any
import yaml

class ConfigLoadError(Exception):
    """Custom exception for config loading errors."""
    pass

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML config file.

    Returns:
        Dict[str, Any]: Dictionary containing config data.

    Raises:
        ConfigLoadError: If the file is missing or has YAML issues.
    """
    if not os.path.isfile(config_path):
        raise ConfigLoadError(f"Config file not found: {config_path}")

    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            if not isinstance(config, dict):
                raise ConfigLoadError("Top-level structure must be a dictionary.")
            return config
    except yaml.YAMLError as e:
        raise ConfigLoadError(f"YAML parsing error: {e}")
    except Exception as e:
        raise ConfigLoadError(f"Unexpected error while loading config: {e}")
