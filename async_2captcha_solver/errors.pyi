from _typeshed import Incomplete as Incomplete

class CaptchaError(Exception):
    message: Incomplete
    error_code: Incomplete
    def __init__(self, msg: str, error_code: int) -> None: ...

class CaptchaUnsolvable(Exception): ...
