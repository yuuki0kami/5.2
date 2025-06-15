try:
    from sortedcontainers import SortedDict
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without sortedcontainers
    from collections import OrderedDict

    class SortedDict(OrderedDict):
        """Minimal fallback for :class:`sortedcontainers.SortedDict`.

        Maintains keys in sorted order after insertions and updates.
        Only implements the subset of the API used in this project."""

        def __init__(self, *args, **kwargs):
            super().__init__()
            if args or kwargs:
                self.update(*args, **kwargs)

        def __setitem__(self, key, value):
            super().__setitem__(key, value)
            self._reorder()

        def update(self, *args, **kwargs):
            super().update(*args, **kwargs)
            self._reorder()

        def _reorder(self):
            items = sorted(super().items(), key=lambda kv: kv[0])
            super().clear()
            super().update(items)
