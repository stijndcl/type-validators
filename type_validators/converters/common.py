from abc import ABC, abstractmethod
from typing import Any


class Converter(ABC):
    """Main converter class that all other converters inherit from"""
    @abstractmethod
    def convert(self, value: Any) -> Any: ...
