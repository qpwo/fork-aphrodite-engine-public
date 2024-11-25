from typing_extensions import TypedDict

class Passthru(TypedDict):
    """
    (development only) arguments passed through to the model.forward call from the API
    """
    foo: int
    bar: str
