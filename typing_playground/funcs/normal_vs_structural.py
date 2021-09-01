# Initially PEP 484 defined Python static type system as using nominal subtyping. 
# This means that a class A is allowed where a class B is expected if 
# and only if A is a subclass of B.

# This requirement previously also applied to abstract base classes, 
# such as Iterable. The problem with this approach is that a class 
# had to be explicitly marked to support them, which is unpythonic 
# and unlike what one would normally do in idiomatic dynamically 
# typed Python code. For example, this conforms to PEP 484:

from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

# PEP 544 allows to solve this problem by allowing users to write 
# the above code without explicit base classes in the class definition, 
# allowing Bucket to be implicitly considered a subtype of both 
# Sized and Iterable[int] by static type checkers. This is known as 
# structural subtyping (or static duck-typing):

from collections.abc import Iterator, Iterable

class Bucket:  # Note: no base classes
    ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...
result = collect(Bucket())  # Passes type check

# Moreover, by subclassing a special class Protocol, a user can define new custom 
# protocols to fully enjoy structural subtyping (see examples below).