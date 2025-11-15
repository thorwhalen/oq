"""plotly.express"""

from contextlib import suppress
from guide.tools import submodule_callables

with suppress(ImportError, ModuleNotFoundError):
    import plotly.express

    for _ in list(dict.fromkeys(submodule_callables(plotly.express))):
        if hasattr(_, "__name__"):
            locals()[_.__name__] = _
