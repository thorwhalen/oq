"""Configuration management for OQ package."""

import json
from pathlib import Path
from typing import Dict, List, Any
from contextlib import suppress

# Default module mapping
MODULE_MAPPING = {
    "np": "numpy",
    "pd": "pandas",
    "sp": "scipy",
    "plt": "matplotlib.pyplot",
    "sns": "seaborn",
    "sk": "sklearn",
    "xgb": "xgboost",
    "lgb": "lightgbm",
    "torch": "torch",
    "tf": "tensorflow",
    "px": "plotly.express",
    "sm": "statsmodels",
}


def get_default_config() -> Dict[str, Any]:
    """Load the default configuration from the package data directory.

    Returns:
        Dictionary containing the default configuration.
    """
    from importlib.resources import files

    config_path = files("oq") / "data" / "default_config.json"

    with suppress(FileNotFoundError, json.JSONDecodeError):
        with open(config_path, "r") as f:
            return json.load(f)

    # Fallback default configuration
    return {
        "import_config": {
            "auto_import_to_root": True,
            "module_order": list(MODULE_MAPPING.keys()),
            "enabled_modules": {mod: True for mod in MODULE_MAPPING},
        }
    }


def get_user_config() -> Dict[str, Any]:
    """Load user configuration if it exists.

    Returns:
        Dictionary containing user configuration, or empty dict if not found.
    """
    from .util import get_config

    with suppress(Exception):
        # Only try to get config if it exists, don't prompt
        import os
        from config2py import get_app_config_folder

        config_dir = os.environ.get('OQ_APP_DATA_DIR', get_app_config_folder('oq'))
        config_file = os.path.join(config_dir, 'import_config.json')

        if os.path.exists(config_file):
            user_config = get_config("import_config")
            if user_config:
                return {"import_config": user_config}

    return {}


def get_config() -> Dict[str, Any]:
    """Get merged configuration (user config overrides defaults).

    Returns:
        Merged configuration dictionary.
    """
    config = get_default_config()
    user_config = get_user_config()

    # Merge configs (user overrides default)
    if "import_config" in user_config:
        config["import_config"].update(user_config["import_config"])

    return config


def get_import_order() -> List[str]:
    """Get the ordered list of modules to import.

    Returns:
        List of module short names in import order.
    """
    config = get_config()
    import_config = config.get("import_config", {})
    module_order = import_config.get("module_order", list(MODULE_MAPPING.keys()))
    enabled_modules = import_config.get(
        "enabled_modules", {mod: True for mod in MODULE_MAPPING}
    )

    # Filter to only enabled modules
    return [mod for mod in module_order if enabled_modules.get(mod, True)]


def should_auto_import() -> bool:
    """Check if auto-import to root namespace is enabled.

    Returns:
        True if auto-import is enabled, False otherwise.
    """
    config = get_config()
    return config.get("import_config", {}).get("auto_import_to_root", True)
