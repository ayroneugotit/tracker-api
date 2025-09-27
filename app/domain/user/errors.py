from dataclasses import dataclass


@dataclass(frozen=True)
class AuthError:
    status_code: int
    detail: str
