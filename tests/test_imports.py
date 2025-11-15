"""Test basic import functionality."""

import pytest
from contextlib import suppress


def test_basic_import():
    """Test that oq can be imported."""
    import oq

    assert oq is not None


def test_util_import():
    """Test that util module can be imported."""
    from oq import util

    assert util is not None
    assert hasattr(util, "get_config")
    assert hasattr(util, "pkg_name")
    assert util.pkg_name == "oq"


def test_config_import():
    """Test that config module can be imported."""
    from oq import config

    assert config is not None
    assert hasattr(config, "get_config")
    assert hasattr(config, "get_import_order")
    assert hasattr(config, "should_auto_import")


def test_module_imports():
    """Test that wrapper modules can be imported (if their dependencies exist)."""
    module_names = ["np", "pd", "sp", "plt", "sns", "sk", "xgb", "lgb", "torch", "tf", "px", "sm"]

    for mod_name in module_names:
        # These should never raise an error, even if the underlying library isn't installed
        with suppress(ImportError, ModuleNotFoundError):
            module = __import__(f"oq.{mod_name}", fromlist=[mod_name])
            assert module is not None


def test_numpy_available():
    """Test numpy module if numpy is installed."""
    try:
        import numpy
    except ImportError:
        pytest.skip("numpy not installed")

    from oq import np

    # Test that we have numpy functions
    assert hasattr(np, "array")
    assert hasattr(np, "mean")
    assert callable(np.array)


def test_pandas_available():
    """Test pandas module if pandas is installed."""
    try:
        import pandas
    except ImportError:
        pytest.skip("pandas not installed")

    from oq import pd

    # Test that we have pandas objects
    assert hasattr(pd, "DataFrame")
    assert hasattr(pd, "Series")
    assert callable(pd.DataFrame)


def test_sklearn_available():
    """Test sklearn module if sklearn is installed."""
    try:
        import sklearn
    except ImportError:
        pytest.skip("sklearn not installed")

    from oq import sk

    # Test that we have sklearn objects
    # Note: exact objects depend on sklearn version, so we just check the module exists
    assert sk is not None


def test_no_import_errors_on_missing_dependencies():
    """Test that missing dependencies don't break the package."""
    # This should work even if no scientific libraries are installed
    import oq

    assert oq is not None
    # Util should always be available
    assert hasattr(oq, "util")
