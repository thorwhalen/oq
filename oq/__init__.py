"""OQ - Objects Quickly.

Quick access to popular data science and machine learning libraries.

Usage:
    # Import specific module
    from oq import pd
    df = pd.DataFrame({'a': [1, 2, 3]})

    # Import everything (if auto_import_to_root is True in config)
    import oq
    df = oq.DataFrame({'a': [1, 2, 3]})  # pandas DataFrame
    arr = oq.array([1, 2, 3])  # numpy array

Module abbreviations:
    - np: numpy
    - pd: pandas
    - sp: scipy
    - plt: matplotlib.pyplot
    - sns: seaborn
    - sk: sklearn (scikit-learn)
    - xgb: xgboost
    - lgb: lightgbm
    - torch: PyTorch
    - tf: TensorFlow
    - px: plotly.express
    - sm: statsmodels
"""

from contextlib import suppress

# Always expose submodules for explicit imports
from . import util  # noqa: F401

# Optional imports - only if packages are installed
with suppress(ImportError, ModuleNotFoundError):
    from . import np  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import pd  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import sp  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import plt  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import sns  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import sk  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import xgb  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import lgb  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import torch  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import tf  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import px  # noqa: F401

with suppress(ImportError, ModuleNotFoundError):
    from . import sm  # noqa: F401


# Auto-import to root namespace if configured
def _populate_root_namespace():
    """Populate root namespace with objects from enabled modules."""
    from . import config

    if not config.should_auto_import():
        return

    import sys

    module_order = config.get_import_order()
    current_module = sys.modules[__name__]

    for mod_name in module_order:
        with suppress(ImportError, ModuleNotFoundError, AttributeError):
            # Import the submodule
            submodule = __import__(f"oq.{mod_name}", fromlist=[mod_name])

            # Get all public attributes from the submodule
            for attr_name in dir(submodule):
                if not attr_name.startswith("_"):
                    attr = getattr(submodule, attr_name)
                    # Only add callables and classes
                    if callable(attr):
                        setattr(current_module, attr_name, attr)


# Perform auto-import
_populate_root_namespace()

# Clean up the namespace
del _populate_root_namespace
