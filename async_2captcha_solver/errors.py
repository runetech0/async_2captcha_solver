

class CaptchaError(Exception):
    def __init__(self, msg: str, error_code: int) -> None:
        self.message = msg
        self.error_code = error_code

    def __repr__(self) -> str:
        return f"{self.error_code}: {self.message}"

    def __str__(self) -> str:
        return f"{self.error_code}: {self.message}"


class CaptchaUnsolvable(Exception):
    """Captcha is not solveable"""
