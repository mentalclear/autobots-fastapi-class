# Generics

# Since type information about objects kept in containers cannot be statically 
# inferred in a generic way, abstract base classes have been extended to 
# support subscription to denote expected types for container elements.

from collections.abc import Mapping, Sequence

class Employee:
    pass

def notify_by_mail(employees: Sequence[Employee], overrides: Mapping[str, str]) -> None:
    pass

# Generics can be parameterized by using a new factory
# available in typing called TypeVar.

from typing import Generic, TypeVar

T = TypeVar('T') # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]

# User-defined generic types

# A user-defined class can be defined as a generic class.
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Ser ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

# Generic[T] as a base class defines that the class LoggedVar takes 
# a single type parameter T . This also makes T valid as a type within 
# the class body.        

# The Generic base class defines __class_getitem__() so that LoggedVar[t] 
# is valid as a type:

from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

# A generic type can have any number of type variables, 
# and type variables may be constrained:

T = TypeVar('T')
S = TypeVar('S', int, str)

class StrangePair(Generic[T, S]):
    pass

# Each type variable argument to Generic must be distinct. This is thus invalid:

# class Pair(Generic[T, T]):   # INVALID
#     pass

# TypeError: Parameters to Generic[...] must all be unique


# You can use multiple inheritance with Generic:
from collections.abc import Sized

T = TypeVar('T')

class LinkedList(Sized, Generic[T]):
    pass

# When inheriting from generic classes, some type variables could be fixed:

T = TypeVar('T')

class MyDict(Mapping[str, T]):
    pass

# In this case MyDict has a single parameter, T.

# Using a generic class without specifying type parameters assumes Any for each 
# position. In the following example, MyIterable is not generic but 
# implicitly inherits from Iterable[Any]:

class MyIterable(Iterable): # Same as Iterable[Any]
    pass

# User defined generic type aliases are also supported. Examples:
from typing import Union
S = TypeVar('S')
Response = Union[Iterable[S], int]

# Return type here is same as Union[Iterable[str], int]
def response(query: str) -> Response[str]:
    pass

T = TypeVar('T', int, float, complex)
Vec = Iterable[tuple[T, T]]

def inproduct(v: Vec[T]) -> T: # Same as Iterable[tuple[T, T]]
    return sum(x*y for x, y in v)


