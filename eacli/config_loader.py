"""Utilities for loading and managing app configuration."""
import json
from pathlib import Path


def load_config():
    """Load apps configuration from config.json."""
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path, "r") as f:
        return json.load(f)


def get_enabled_apps():
    """Get list of enabled apps from configuration."""
    config = load_config()
    return [app for app in config["apps"] if app.get("enabled", False)]
