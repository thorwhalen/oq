"""scipy"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import scipy

    for _ in list(dict.fromkeys(submodule_callables(scipy))):
        if hasattr(_, "__name__"):
            locals()[_.__name__] = _
