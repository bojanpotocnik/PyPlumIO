"""Contains versions structure parser."""

import struct
from typing import Any, Dict, Final, Optional, Tuple

MODULE_A: Final = "module_a"
MODULE_B: Final = "module_b"
MODULE_C: Final = "module_c"
MODULE_LAMBDA: Final = "module_lambda"
MODULE_ECOSTER: Final = "module_ecoster"
MODULE_PANEL: Final = "module_panel"
MODULES: Final = (
    MODULE_A,
    MODULE_B,
    MODULE_C,
    MODULE_LAMBDA,
    MODULE_ECOSTER,
    MODULE_PANEL,
)


def from_bytes(
    message: bytearray, offset: int = 0, data: Dict[str, Any] = None
) -> Tuple[Dict[str, Any], int]:
    """Parses frame message into usable data.

    Keyword arguments:
        message -- message bytes
        offset -- current data offset
    """
    if data is None:
        data = {}

    for module in MODULES:
        data[module], offset = _parse_module_version(module, message, offset)

    return data, offset


def _parse_module_version(
    module: str, message: bytearray, offset: int = 0
) -> Tuple[Optional[str], int]:
    """Gets module version by module name.

    Keyword arguments:
        module - module name
        message - bytes to parse module version from
        offset - message offset
    """
    if message[offset] == 0xFF:
        return None, (offset + 1)

    version_data = struct.unpack("<BBB", message[offset : offset + 3])
    module_version = ".".join(str(i) for i in version_data)
    offset += 3

    if module == MODULE_A:
        vendor_code, vendor_version = struct.unpack("<BB", message[offset : offset + 2])
        module_version += f".{chr(vendor_code)}{str(vendor_version)}"
        offset += 2

    return module_version, offset
