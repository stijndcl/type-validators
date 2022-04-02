# type-validators

Python utility package to validate values based on type annotations

## Usage

To add a validator or converter, annotate the argument as ``typing.Annotated``. This is a generic type that requires the
first argument to be the actual type you want, with additional metadata afterwards. Pass any converters or validators
after the type. Next, add the `@validate`-decorator to your function to allow pre-processing of the arguments.

```python
from typing import Annotated
from type_validators.validators.numeric import Below
from type_validators import validate


@validate
def some_function(arg: Annotated[int, Below(20)]):
    """
    :param arg: an int that should be less than 20.
    """
```

You can add any amount of converters and validators to a type annotation. These are processed from **left to right**.

```python
from typing import Annotated
from type_validators.converters.strings import Upper
from type_validators.validators.strings import Matches
from type_validators import validate


@validate
def some_function(arg: Annotated[str, Matches(r"^[a-zA-Z].*"), Upper()]):
    """
    :param arg: a string that should start with a letter, and will
                then be converted to uppercase
    """
```