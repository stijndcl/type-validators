from type_validators.converters.common import Converter


class Lower(Converter):
    """Converts a string argument to lowercase"""
    def convert(self, value: str) -> str:
        return value.lower()


class Upper(Converter):
    """Converts a string argument to uppercase"""
    def convert(self, value: str) -> str:
        return value.upper()
