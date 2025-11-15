"""sk (scikit-learn)"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import sklearn

    # Filter out unhashable items before using dict.fromkeys
    callables = submodule_callables(sklearn)
    hashable_callables = []
    for item in callables:
        try:
            hash(item)
            hashable_callables.append(item)
        except TypeError:
            pass  # Skip unhashable items

    for _ in list(dict.fromkeys(hashable_callables)):
        if hasattr(_, "__name__"):
            locals()[_.__name__] = _

    for _subpackage_name in sklearn.__all__:
        with suppress(ModuleNotFoundError):
            _subpackage = __import__(f"sklearn.{_subpackage_name}")
            for _ in submodule_callables(sklearn):
                if hasattr(_, "__name__"):
                    locals()[_.__name__] = _
