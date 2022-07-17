"""Contains tests for thermostats structure."""

from pyplumio.const import ATTR_THERMOSTATS
from pyplumio.structures.thermostats import from_bytes

_message = bytearray.fromhex("05010300002E4200004842")
_data = {
    ATTR_THERMOSTATS: [
        {"contacts": True, "schedule": False, "mode": 3, "target": 50.0, "temp": 43.5}
    ]
}


def test_from_bytes() -> None:
    """Test conversion from bytes."""
    data, offset = from_bytes(_message)
    assert data == _data
    assert offset == 11
