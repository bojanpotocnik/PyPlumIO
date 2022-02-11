"""Contains connection shortcuts and version information."""

from __future__ import annotations

from collections.abc import Callable

from .devices import DevicesCollection
from .econet import EcoNET, SerialConnection, TcpConnection
from .version import __version__  # noqa


def tcp(
    callback: Callable[[DevicesCollection, EcoNET], None],
    host: str,
    port: int,
    interval: int = 1,
    **kwargs,
):
    """Shortcut for TCP connection.

    Keyword arguments:
    callback -- callback method
    host -- device host
    port -- device port
    interval -- callback update interval in seconds
    **kwargs -- keyword arguments for connection driver
    """
    TcpConnection(host, port, **kwargs).run(callback, interval)


def serial(
    callback: Callable[[DevicesCollection, EcoNET], None],
    device: str,
    baudrate: int = 115200,
    interval: int = 1,
    **kwargs,
):
    """Shortcut for serial connection.

    Keyword arguments:
    callback -- callback method
    device -- serial device url, e. g. /dev/ttyUSB0
    baudrate -- serial port baudrate
    interval -- callback update interval in seconds
    **kwargs -- keyword arguments for connection driver
    """
    SerialConnection(device, baudrate, **kwargs).run(callback, interval)
