import inspect
from collections.abc import Callable
from typing import get_type_hints

from type_validators.converters.common import Converter
from type_validators.errors import ValidationError
from type_validators.validators.common import Validator


def validate_values(function: Callable):
    """Decorator to run validation on a function's arguments"""
    type_hints = get_type_hints(function, include_extras=True)
    argspec = inspect.getfullargspec(function)

    def _wrapper(*args, **kwargs):
        # Cast to list because tuples don't support assignment
        args = list(args)

        for index, argument in enumerate(argspec[0]):
            hint = type_hints.get(argument)
            metadata = getattr(hint, "__metadata__", None)

            # No metadata
            if metadata is None:
                continue

            # Run all converters and validators from left to right
            for meta in metadata:
                if isinstance(meta, Converter):
                    args[index] = meta.convert(args[index])
                elif isinstance(meta, Validator):
                    if not meta.validate(args[index]):
                        raise ValidationError(argument=argument, value=args[index])

        return function(*args, **kwargs)
    return _wrapper


# Alias
validate = validate_values
