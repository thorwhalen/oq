"""Test configuration functionality."""

import pytest


def test_get_default_config():
    """Test getting default configuration."""
    from oq.config import get_default_config

    config = get_default_config()
    assert config is not None
    assert "import_config" in config
    assert "auto_import_to_root" in config["import_config"]
    assert "module_order" in config["import_config"]
    assert "enabled_modules" in config["import_config"]


def test_get_config():
    """Test getting merged configuration."""
    from oq.config import get_config

    config = get_config()
    assert config is not None
    assert "import_config" in config


def test_get_import_order():
    """Test getting import order."""
    from oq.config import get_import_order

    order = get_import_order()
    assert isinstance(order, list)
    assert len(order) > 0
    # All items should be strings
    assert all(isinstance(item, str) for item in order)


def test_should_auto_import():
    """Test auto-import flag."""
    from oq.config import should_auto_import

    result = should_auto_import()
    assert isinstance(result, bool)


def test_module_mapping():
    """Test that module mapping is defined correctly."""
    from oq.config import MODULE_MAPPING

    assert isinstance(MODULE_MAPPING, dict)
    assert "np" in MODULE_MAPPING
    assert "pd" in MODULE_MAPPING
    assert MODULE_MAPPING["np"] == "numpy"
    assert MODULE_MAPPING["pd"] == "pandas"


def test_enabled_modules_filtering():
    """Test that enabled_modules filtering works."""
    from oq.config import get_import_order, get_default_config

    config = get_default_config()
    order = get_import_order()

    # All enabled modules should be in the order
    enabled = config["import_config"]["enabled_modules"]
    enabled_list = [k for k, v in enabled.items() if v]

    # Order should only contain enabled modules
    for mod in order:
        assert mod in enabled_list
