"""Test PyPlumIO base frame."""

from typing import ClassVar, Tuple

import pytest

from pyplumio.const import BROADCAST_ADDRESS, ECONET_ADDRESS
from pyplumio.exceptions import UnknownFrameError
from pyplumio.frames import (
    ECONET_TYPE,
    ECONET_VERSION,
    HEADER_SIZE,
    Request,
    RequestTypes,
    Response,
    ResponseTypes,
    get_frame_handler,
    responses,
)


class TestRequest(Request):
    """Test request class."""

    frame_type: ClassVar[int] = RequestTypes.PROGRAM_VERSION


class TestResponse(Response):
    """Test response class."""

    frame_type: ClassVar[int] = ResponseTypes.PROGRAM_VERSION


@pytest.fixture(name="request_")
def fixture_request_() -> Request:
    """Return program version request."""
    return TestRequest()


@pytest.fixture(name="response")
def fixture_response() -> Response:
    """Return program version response."""
    return TestResponse()


@pytest.fixture(name="frames")
def fixture_frames(request_: Request, response: Response) -> Tuple[Request, Response]:
    """Return request and response frames as a tuple."""
    return (request_, response)


@pytest.fixture(name="types")
def fixture_types() -> Tuple[int, int]:
    """Return request and response types as a tuple."""
    return (RequestTypes.PROGRAM_VERSION, ResponseTypes.PROGRAM_VERSION)


def test_get_frame_handler() -> None:
    """Test getting frame handler."""
    assert get_frame_handler(0x18) == "frames.requests.StopMaster"
    with pytest.raises(UnknownFrameError):
        get_frame_handler(0x0)


def test_passing_frame_type(
    frames: Tuple[Request, Response], types: Tuple[int, int]
) -> None:
    """Test getting frame type."""
    for index, frame in enumerate(frames):
        assert frame.frame_type == types[index]


def test_default_params(frames: Tuple[Request, Response]) -> None:
    """Test frame attributes."""
    for frame in frames:
        assert frame.recipient == BROADCAST_ADDRESS
        assert frame.message == b""
        assert frame.sender == ECONET_ADDRESS
        assert frame.sender_type == ECONET_TYPE
        assert frame.econet_version == ECONET_VERSION


def test_frame_length_without_data(frames: Tuple[Request, Response]) -> None:
    """Test frame length without any data."""
    for frame in frames:
        assert frame.length == HEADER_SIZE + 3
        assert len(frame) == HEADER_SIZE + 3


def test_get_header(frames: Tuple[Request, Response]) -> None:
    """Test getting frame header as bytes."""
    for frame in frames:
        assert frame.header == b"\x68\x0a\x00\x00\x56\x30\x05"


def test_base_class_with_message() -> None:
    """Test base request class with message."""
    frame = TestRequest(message=bytearray(b"\xB0\x0B"))
    assert frame.message == b"\xB0\x0B"


def test_to_bytes() -> None:
    """Test conversion to bytes."""
    frame = TestRequest(message=bytearray(b"\xB0\x0B"))
    assert frame.bytes == b"\x68\x0C\x00\x00\x56\x30\x05\x40\xB0\x0B\xFC\x16"


def test_to_hex() -> None:
    """Test conversion to hex."""
    frame = TestRequest(message=bytearray(b"\xB0\x0B"))
    hex_data = ["68", "0C", "00", "00", "56", "30", "05", "40", "B0", "0B", "FC", "16"]
    assert frame.hex == hex_data


def test_equality() -> None:
    """Test equality check."""
    assert responses.ProgramVersion() == responses.ProgramVersion()


def test_request_repr(request_: Request) -> None:
    """Test serialiazible request representation."""
    repr_string = (
        "TestRequest(recipient=0, sender=86, sender_type=48, econet_version=5, "
        + "message=bytearray(b''), data={})"
    )
    assert repr(request_) == repr_string


def test_response_repr(response: Response) -> None:
    """Test serialiazible response representation."""
    repr_string = (
        "TestResponse(recipient=0, sender=86, sender_type=48, econet_version=5, "
        + "message=bytearray(b''), data={})"
    )
    assert repr(response) == repr_string
