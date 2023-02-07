"""Contains connection shortcuts and version information."""
from __future__ import annotations

from pyplumio.connection import Connection, SerialConnection, TcpConnection
from pyplumio.helpers.network_info import EthernetParameters, WirelessParameters
from pyplumio.version import __version__


def serial(*args, **kwargs) -> SerialConnection:
    """Helper function for Serial connection."""
    return SerialConnection(*args, **kwargs)


def tcp(*args, **kwargs) -> TcpConnection:
    """Helper function for TCP connection."""
    return TcpConnection(*args, **kwargs)


def ethernet_parameters(**kwargs) -> EthernetParameters:
    """Return instance of ethernet parameters dataclass."""
    return EthernetParameters(status=True, **kwargs)


def wireless_parameters(**kwargs) -> WirelessParameters:
    """Return instance of wireless parameters dataclass."""
    return WirelessParameters(status=True, **kwargs)


__all__ = [
    "Connection",
    "SerialConnection",
    "TcpConnection",
    "serial",
    "tcp",
    "ethernet_parameters",
    "wireless_parameters",
    "__version__",
]
