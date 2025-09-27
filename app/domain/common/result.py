from typing import TypeVar, Generic, Union
from dataclasses import dataclass

S = TypeVar("S")
F = TypeVar("F")


@dataclass(frozen=True)
class Success(Generic[S]):
    value: S


def success(value: S) -> Success[S]:
    return Success(value)


@dataclass(frozen=True)
class Failure(Generic[F]):
    error: F


def failure(value: F) -> Failure[F]:
    return Failure(value)


Result = Union[Success[S], Failure[F]]
