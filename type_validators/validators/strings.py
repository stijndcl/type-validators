import re
from typing import Union

from type_validators.validators.common import Validator


class Matches(Validator):
    """Check that a string matches a regexp"""
    pattern: Union[str, re.Pattern]
    flags: Union[int, re.RegexFlag]

    def __init__(self, pattern: Union[str, re.Pattern], flags: Union[int, re.RegexFlag] = 0):
        super().__init__()
        self.pattern = pattern
        self.flags = flags

    def validate(self, value: str) -> bool:
        return re.fullmatch(self.pattern, value, self.flags) is not None
