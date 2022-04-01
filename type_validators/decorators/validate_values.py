import inspect
from collections.abc import Callable
from typing import get_type_hints

from type_validators.errors import ValidationError


def validate_values(function: Callable):
    """Decorator to run validation on a function's arguments"""
    type_hints = get_type_hints(function, include_extras=True)
    argspec = inspect.getfullargspec(function)

    def _wrapper(*args, **kwargs):
        for index, argument in enumerate(argspec[0]):
            hint = type_hints.get(argument)
            validators = getattr(hint, "__metadata__", None)

            if validators is None:
                continue

            for validator in validators:
                if not validator.validate(args[index]):
                    raise ValidationError(argument, args[index])

        return function(*args, **kwargs)
    return _wrapper


# Alias
validate = validate_values
