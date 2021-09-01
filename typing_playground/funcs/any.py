# A special kind of type is Any. A static type checker will treat 
# every type as being compatible with Any and Any as being 
# compatible with every type.

from typing import Any

a = None    # type: Any
a = []      # OK
a = 2       # OK

s = ''      # type: str
s = a       # OK

def foo(item: Any) -> int:
    # Typechecks; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()


# Furthermore, all functions without a return 
# type or parameter types will implicitly default to using Any:
def legacy_parser(text):
    ...
    return None

# A static type checker will treat the above
# as having the same signature as:
def legacy_parser_any(text: Any) -> Any:
    ...
    return None

# This behavior allows Any to be used as an escape hatch when you need 
# to mix dynamically and statically typed code.

# Contrast the behavior of Any with the behavior of object. Similar to Any, 
# every type is a subtype of object. However, unlike Any, the reverse 
# is not true: object is not a subtype of every other type.        


def hash_a(item: object) -> int:
    # Fails; an object does not have a 'magic' method.
    item.magic()
    ...

def hash_b(item: Any) -> int:
    # Typechecks
    item.magic()
    ...

# Typechecks, since ints and strs are subclasses of object
hash_a(42)
hash_a("foo")

# Typechecks, since Any is compatible with all types
hash_b(42)
hash_b("foo")



