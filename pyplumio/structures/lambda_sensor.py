"""Contains a lambda sensor structure decoder."""
from __future__ import annotations

from contextlib import suppress
import math
from typing import Any, Final

from pyplumio.const import BYTE_UNDEFINED, LambdaState
from pyplumio.helpers.data_types import UnsignedShort
from pyplumio.structures import StructureDecoder
from pyplumio.utils import ensure_dict

ATTR_LAMBDA_STATE: Final = "lambda_state"
ATTR_LAMBDA_TARGET: Final = "lambda_target"
ATTR_LAMBDA_LEVEL: Final = "lambda_level"


class LambdaSensorStructure(StructureDecoder):
    """Represents a lambda sensor data structure."""

    __slots__ = ()

    def decode(
        self, message: bytearray, offset: int = 0, data: dict[str, Any] | None = None
    ) -> tuple[dict[str, Any], int]:
        """Decode bytes and return message data and offset."""
        lambda_state = message[offset]
        offset += 1
        if lambda_state == BYTE_UNDEFINED:
            return ensure_dict(data), offset

        with suppress(ValueError):
            lambda_state = LambdaState(lambda_state)

        lambda_target = message[offset]
        offset += 1
        level = UnsignedShort.from_bytes(message, offset)
        offset += level.size
        return (
            ensure_dict(
                data,
                {
                    ATTR_LAMBDA_STATE: lambda_state,
                    ATTR_LAMBDA_TARGET: lambda_target,
                    ATTR_LAMBDA_LEVEL: None
                    if math.isnan(level.value)
                    else (level.value / 10),
                },
            ),
            offset,
        )
