"""Central registry of all LangGraph‑style agents.

Each agent module provides a ``compiled`` object that mimics the ``LangGraph``
compiled graph.  The registry maps a short name (e.g., ``"tomas"``) to the
corresponding compiled instance.  This allows other parts of the application to
lookup agents dynamically.
"""

from .tomas.stategraph import compiled as tomas_compiled
from .cto.stategraph import compiled as cto_compiled
from .cpo.stategraph import compiled as cpo_compiled
from .cmo.stategraph import compiled as cmo_compiled
from .cfo.stategraph import compiled as cfo_compiled
from .director.stategraph import compiled as director_compiled
from .specialist.stategraph import compiled as specialist_compiled

AGENT_REGISTRY = {
    "tomas": tomas_compiled,
    "cto": cto_compiled,
    "cpo": cpo_compiled,
    "cmo": cmo_compiled,
    "cfo": cfo_compiled,
    "director": director_compiled,
    "specialist": specialist_compiled,
}
