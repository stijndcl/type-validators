from collections.abc import Iterable, Sized

from type_validators.validators.common import Validator


class AnyOf(Validator):
    """Check that a value is included in an iterable of allowed values"""
    allowed_values: Iterable

    def __init__(self, allowed_values: Iterable):
        super().__init__()
        self.allowed_values = allowed_values

    def validate(self, value) -> bool:
        return value in self.allowed_values


class MinLen(Validator):
    """Check that an iterable has a minimum length"""
    length: int

    def __init__(self, length: int):
        super().__init__()
        self.length = length

    def validate(self, value: Sized) -> bool:
        return len(value) >= self.length


class MaxLen(Validator):
    """Check that an iterable has a maximum length"""
    length: int

    def __init__(self, length: int):
        super().__init__()
        self.length = length

    def validate(self, value: Sized) -> bool:
        return len(value) <= self.length
