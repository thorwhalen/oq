"""Test actual functionality with real libraries."""

import pytest


def test_numpy_functionality():
    """Test that numpy functions work through oq.np."""
    try:
        import numpy
    except ImportError:
        pytest.skip("numpy not installed")

    from oq import np

    # Create array
    arr = np.array([1, 2, 3, 4, 5])
    assert arr is not None

    # Test a numpy function
    mean_val = np.mean(arr)
    assert mean_val == 3.0


def test_pandas_functionality():
    """Test that pandas functions work through oq.pd."""
    try:
        import pandas
    except ImportError:
        pytest.skip("pandas not installed")

    from oq import pd

    # Create DataFrame
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert df is not None
    assert len(df) == 3

    # Test a pandas function
    assert hasattr(df, "mean")


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


def test_root_import_pandas():
    """Test that pandas functions are available at root if pandas is installed."""
    try:
        import pandas
    except ImportError:
        pytest.skip("pandas not installed")

    import oq

    # Check if DataFrame is available (should be if auto_import is True)
    if hasattr(oq, "DataFrame"):
        df = oq.DataFrame({"a": [1, 2, 3]})
        assert df is not None
        assert len(df) == 3


def test_multiple_libraries():
    """Test using multiple libraries together."""
    try:
        import numpy
        import pandas
    except ImportError:
        pytest.skip("numpy or pandas not installed")

    from oq import np, pd

    # Create numpy array
    arr = np.array([1, 2, 3, 4, 5])

    # Create pandas DataFrame from numpy array
    df = pd.DataFrame(arr, columns=["values"])

    assert len(df) == 5
    assert df["values"].sum() == 15
