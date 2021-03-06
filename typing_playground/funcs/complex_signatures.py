from collections.abc import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    pass

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message_explained(
    message: str, 
    servers: Sequence[tuple[tuple[str, int], dict[str,str]]])  -> None:
    pass

# Note that None as a type hint is a special case and is replaced by type(None).



