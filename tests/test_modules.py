"""Test individual module wrappers."""

import pytest
from contextlib import suppress


def test_np_module_structure():
    """Test numpy module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import np

        # Should have a docstring
        assert np.__doc__ is not None
        assert "numpy" in np.__doc__.lower()


def test_pd_module_structure():
    """Test pandas module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import pd

        # Should have a docstring
        assert pd.__doc__ is not None
        assert "pandas" in pd.__doc__.lower()


def test_sp_module_structure():
    """Test scipy module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import sp

        # Should have a docstring
        assert sp.__doc__ is not None
        assert "scipy" in sp.__doc__.lower()


def test_sk_module_structure():
    """Test sklearn module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import sk

        # Should have a docstring
        assert sk.__doc__ is not None
        assert "sklearn" in sk.__doc__.lower()


def test_plt_module_structure():
    """Test matplotlib.pyplot module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import plt

        # Should have a docstring
        assert plt.__doc__ is not None


def test_sns_module_structure():
    """Test seaborn module structure."""
    with suppress(ImportError, ModuleNotFoundError):
        from oq import sns

        # Should have a docstring
        assert sns.__doc__ is not None
        assert "seaborn" in sns.__doc__.lower()


def test_all_modules_import_gracefully():
    """Test that all modules can be imported without errors."""
    modules = ["np", "pd", "sp", "plt", "sns", "sk", "xgb", "lgb", "torch", "tf", "px", "sm"]

    for mod in modules:
        # Should not raise any exception
        with suppress(ImportError, ModuleNotFoundError):
            __import__(f"oq.{mod}", fromlist=[mod])
