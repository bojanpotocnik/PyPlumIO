"""Contains lambda structure decoder."""
from __future__ import annotations

from typing import Optional, Tuple

from pyplumio.const import ATTR_LOAD, BYTE_UNDEFINED
from pyplumio.helpers.typing import DeviceDataType
from pyplumio.structures import StructureDecoder


class LoadStructure(StructureDecoder):
    """Represents load sensor data structure."""

    def decode(
        self, message: bytearray, offset: int = 0, data: Optional[DeviceDataType] = None
    ) -> Tuple[DeviceDataType, int]:
        """Decode bytes and return message data and offset."""
        if message[offset] != BYTE_UNDEFINED:
            data[ATTR_LOAD] = message[offset]

        return data, offset + 1
