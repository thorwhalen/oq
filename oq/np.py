"""numpy"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import numpy

    # Filter out unhashable items before using dict.fromkeys
    callables = submodule_callables(numpy)
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
