from pyplumio import econet_serial_connection, econet_tcp_connection
from pyplumio.econet import SerialConnection, TcpConnection


def test_econet_tcp_connection():
    econet = econet_tcp_connection(host="localhost", port=8899)
    assert isinstance(econet, TcpConnection)


def test_econet_serial_connection():
    econet = econet_serial_connection(device="/dev/ttyUSB0")
    assert isinstance(econet, SerialConnection)
