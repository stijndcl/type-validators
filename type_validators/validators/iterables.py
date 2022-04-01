from collections.abc import Iterable
from type_validators.validators.common import Validator


class AnyOf(Validator):
    """Check that a value is included in an iterable of allowed values"""
    allowed_values: Iterable

    def __init__(self, allowed_values: Iterable):
        super().__init__()
        self.allowed_values = allowed_values

    def validate(self, value) -> bool:
        return value in self.allowed_values