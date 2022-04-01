from type_validators.types import Comparable
from type_validators.validators.common import Validator


class LessThan(Validator):
    """Check if a value is less than a given upper bound"""
    bound: Comparable
    inclusive: bool

    def __init__(self, bound: Comparable, inclusive: bool = False):
        super().__init__()
        self.bound = bound
        self.inclusive = inclusive

    def validate(self, value: Comparable) -> bool:
        if self.inclusive:
            return value <= self.bound

        return value < self.bound


class GreaterThan(Validator):
    """Check if a value is higher than a given lower bound"""
    bound: Comparable
    inclusive: bool

    def __init__(self, bound: Comparable, inclusive: bool = False):
        super().__init__()
        self.bound = bound
        self.inclusive = inclusive

    def validate(self, value: Comparable) -> bool:
        if self.inclusive:
            return value >= self.bound

        return value > self.bound


class InRange(Validator):
    """Check if a value falls between two bounds (inclusive)"""
    lower: Comparable
    upper: Comparable

    def __init__(self, lower: Comparable, upper: Comparable):
        super().__init__()
        self.lower = lower
        self.upper = upper

    def validate(self, value: Comparable) -> bool:
        return self.lower <= value <= self.upper


# Aliases
Between = InRange
Above = GreaterThan
Greater = GreaterThan
Below = LessThan
Smaller = LessThan
