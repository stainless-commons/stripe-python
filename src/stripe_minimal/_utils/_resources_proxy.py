from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `stripe_minimal.resources` module.

    This is used so that we can lazily import `stripe_minimal.resources` only when
    needed *and* so that users can just import `stripe_minimal` and reference `stripe_minimal.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("stripe_minimal.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
