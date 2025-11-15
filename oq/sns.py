"""seaborn"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import seaborn

    for _ in list(dict.fromkeys(submodule_callables(seaborn))):
        if hasattr(_, "__name__"):
            locals()[_.__name__] = _
