"""
Convenience wrappers to make using the conf system as easy and seamless as possible
"""
import warnings
from typing import Any
from typing import Dict
from typing import List


def integrate(
    hub: "pop.hub.Hub",
    imports: List[str] or str,
    override: Dict[str, Any] = None,
    cli: str = None,
    roots: bool = None,
    loader: str = "json",
    logs: bool = True,
):
    """
    Load the conf sub and run the integrate sequence.
    """
    warnings.warn("Use `hub.pop.config.load()` instead", DeprecationWarning)
    hub.pop.sub.add("pop_conf.conf")
    hub.conf.integrate.load(
        imports, override, cli=cli, roots=roots, loader=loader, logs=logs
    )
