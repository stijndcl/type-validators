from abc import abstractmethod, ABCMeta
from typing import TypeVar, Any


class _Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...


Comparable = TypeVar("Comparable", bound=_Comparable)
