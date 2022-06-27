"""Contains serial connection example."""
from __future__ import annotations

import asyncio

import pyplumio


async def main() -> None:
    """Connect and print out device sensors and parameters."""
    async with pyplumio.open_serial_connection("/dev/ttyUSB0", 115200) as connection:
        device = connection.wait_for_device("ecomax")
        sensors = await device.get_value("sensors")
        parameters = await device.get_value("parameters")

    print(sensors)
    print(parameters)


asyncio.run(main())
