"""Test actual functionality with real libraries."""

import pytest


def test_root_import_numpy():
    """Test that numpy functions are available at root if numpy is installed."""
    try:
        import numpy
    except ImportError:
        pytest.skip("numpy not installed")

    import oq

    # Check if array is available (should be if auto_import is True)
    if hasattr(oq, "array"):
        arr = oq.array([1, 2, 3])
        assert arr is not None
