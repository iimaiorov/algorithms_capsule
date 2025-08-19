from typing import Iterable, List, TypeVar

T = TypeVar("T")


def flatten(nested: Iterable[Iterable[T]]) -> List[T]:
    """Flatten a nested iterable into a list."""
    return [item for sub in nested for item in sub]
