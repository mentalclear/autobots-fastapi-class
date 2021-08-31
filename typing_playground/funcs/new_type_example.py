from typing import NewType

# Use the NewType() helper function to create distinct types
UserId = NewType('UserId', int)
some_id = UserId(524313)

# The static type checker will treat the new type as if it were a subclass of the original type. 
# This is useful in helping catch logical errors:

def get_user_name(user_id: UserId) -> str:
    pass

# typechecks
user_a = get_user_name(UserId(42351))

# Doesn't typecheck; an int isn't a UserId
user_b = get_user_name(-1)

# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
print(type(output))

# Note that these checks are enforced only by the static type checker. 
# At runtime, the statement Derived = NewType('Derived', Base) will 
# make Derived a function that immediately returns whatever 
# parameter you pass it. That means the expression Derived(some_value) 
# does not create a new class or introduce any overhead beyond 
# that of a regular function call.

# More precisely, the expression some_value is Derived(some_value) 
# is always true at runtime.

# This also means that it is not possible to create a subtype 
# of Derived since it is an identity function at runtime, 
# not an actual type:

# Fails at runtime and does not typecheck 
# TypeError: function() argument 'code' must be code, not str
#class AdminUserId(UserId): pass

# However, it is possible to create a NewType() based on a ‘derived’ NewType:
ProUserId = NewType('ProUserId', UserId) 