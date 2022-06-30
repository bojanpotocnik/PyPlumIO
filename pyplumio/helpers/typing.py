"""Contains type aliases."""

from typing import Any, Awaitable, Callable, Literal, Tuple, Union

Numeric = Union[int, float]
ParameterTuple = Tuple[int, int, int]
ParameterValue = Union[Literal["off"], Literal["on"], int, float, bool]
ValueCallback = Callable[[Any], Awaitable[Any]]
AsyncCallback = Callable[[], Awaitable[Any]]
