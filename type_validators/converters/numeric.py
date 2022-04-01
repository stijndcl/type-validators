from typing import Any

from type_validators.converters.common import Converter


class Clip(Converter):
    """Keep a value between two bounds"""
    lower: Any
    higher: Any

    def __init__(self, lower: Any, higher: Any):
        super().__init__()
        self.lower = lower
        self.higher = higher

    def convert(self, value: Any) -> Any:
        if value < self.lower:
            return self.lower

        if value > self.higher:
            return self.higher

        return value
