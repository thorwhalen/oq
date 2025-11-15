"""matplotlib.pyplot"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import matplotlib.pyplot

    for _ in list(dict.fromkeys(submodule_callables(matplotlib.pyplot))):
        if hasattr(_, "__name__"):
            locals()[_.__name__] = _
