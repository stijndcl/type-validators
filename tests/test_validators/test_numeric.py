from typing import Annotated

import pytest

from type_validators import validate
from type_validators.errors import ValidationError
from type_validators.validators import numeric


@validate
def _below(_: Annotated[int, numeric.Below(10)]):
    pass


def test_less_than_invalid():
    with pytest.raises(ValidationError):
        _below(11)
