from pyplumio.constants import MODULE_A, MODULE_PANEL
from pyplumio.structures import modules

_message = bytearray([0x1, 0xD, 0x5, 0x5A, 0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x2, 0x3, 0x2B])
_data = {
    MODULE_A: "1.13.5.Z1",
    MODULE_PANEL: "2.3.43",
}


def test_from_bytes():
    data, offset = modules.from_bytes(_message)
    assert data == _data
    assert offset == 12
