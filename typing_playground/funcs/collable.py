from collections.abc import Callable
from typing_extensions import ParamSpecKwargs

# Frameworks expecting callback functions of specific signatures 
# might be type hinted using Callable[[Arg1Type, Arg2Type], ReturnType].

def feeder(get_next_item: Callable[[], str]) -> None:
    # body
    pass

def async_query(
    on_success: Callable[[int], None], 
    on_error: Callable[[int, Exception], None ]) -> None:
    # Body
    pass

# It is possible to declare the return type of a callable without specifying the call 
# signature by substituting a literal ellipsis for the list of arguments in 
# the type hint: Callable[..., ReturnType].
