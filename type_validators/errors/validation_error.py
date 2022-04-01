from typing import Any


class ValidationError(ValueError):
    """Error raised when validation of an argument fails"""
    argument: str
    value: Any

    def __init__(self, argument: str, value: Any):
        super().__init__(f"Invalid value \"{value}\" for argument \"{argument}\".")

        self.argument = argument
        self.value = value
