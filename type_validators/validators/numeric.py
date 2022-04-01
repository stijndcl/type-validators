from typing import Any

from type_validators.validators.common import Validator


class LessThan(Validator):
    """Check if a value is less than a given upper bound"""
    bound: Any
    inclusive: bool

    def __init__(self, bound: Any, inclusive: bool = False):
        super().__init__()
        self.bound = bound
        self.inclusive = inclusive

    def validate(self, value: Any) -> bool:
        if self.inclusive:
            return value <= self.bound

        return value < self.bound


class GreaterThan(Validator):
    """Check if a value is higher than a given lower bound"""
    bound: Any
    inclusive: bool

    def __init__(self, bound: Any, inclusive: bool = False):
        super().__init__()
        self.bound = bound
        self.inclusive = inclusive

    def validate(self, value: Any) -> bool:
        if self.inclusive:
            return value >= self.bound

        return value > self.bound


class InRange(Validator):
    """Check if a value falls between two bounds (inclusive)"""
    lower: Any
    upper: Any

    def __init__(self, lower: Any, upper: Any):
        super().__init__()
        self.lower = lower
        self.upper = upper

    def validate(self, value: Any) -> bool:
        return self.lower <= value <= self.upper


# Aliases
Between = InRange
Above = GreaterThan
Greater = GreaterThan
Below = LessThan
Smaller = LessThan
