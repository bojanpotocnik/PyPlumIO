"""Contains frame class."""

from __future__ import annotations

from . import util
from .constants import (
    BROADCAST_ADDRESS,
    ECONET_ADDRESS,
    ECONET_TYPE,
    ECONET_VERSION,
    FRAME_END,
    FRAME_START,
    HEADER_SIZE,
)


class Frame:
    """Used as base class for creating and parsing request and response
    frames.
    """

    def __init__(self, type_: int = None, recipient: int = BROADCAST_ADDRESS,
            message: bytearray = bytearray(),
            sender: int = ECONET_ADDRESS,
            sender_type: int = ECONET_TYPE,
            econet_version: int = ECONET_VERSION, data = None):
        """Creates new Frame object.

        Keyword arguments:
            type_ -- integer repsentation of frame type
            recipient -- integer repsentation of recipient address
            message -- frame body as bytearray
            sender -- integer respresentation of sender address
            sender_type -- sender type
            econet_version -- version of econet protocol
            data -- frame data, that is used to construct frame message
        """
        self._data = data
        self.recipient = recipient
        self.sender = sender
        self.sender_type = sender_type
        self.econet_version = econet_version
        if type_ is not None:
            self.type_ = type_

        if not message:
            # If frame message is not passed in constructor.
            try:
                self.message = self.create_message()
            except NotImplementedError:
                self.message = bytearray()

        else:
            self.message = message

        self.length = HEADER_SIZE + 1 + len(self.message) + 1 + 1

    def __repr__(self) -> str:
        """Creates readable frame respresentation."""
        name = self.__class__.__name__
        module = self.__module__.rsplit('.', maxsplit=1)[-1]

        return f'{module[:-1]}: {name}'

    def __len__(self) -> int:
        """Returns frame length."""
        return len(self.to_bytes())

    def data(self):
        """Gets data parsed from frame."""
        if self._data is None:
            # If frame data not present.
            self.parse_message(self.message)

        return self._data

    def header(self) -> bytearray:
        """Gets frame header as bytearray."""
        buffer = bytearray(HEADER_SIZE)
        util.pack_header(buffer, 0, *[
            FRAME_START,
            self.length,
            self.recipient,
            self.sender,
            self.sender_type,
            self.econet_version
        ])

        return buffer

    def is_type(self, *types: [Frame]) -> bool:
        """Checks if frame belongs to one of specified types.

        Keyword arguments:
        types -- a list of Frame classes to check against
        """
        for type_ in types:
            if isinstance(self, type_):
                return True

        return False

    def to_bytes(self) -> bytes:
        """Converts frame to bytes respresentation."""
        data = self.header()
        data.append(self.type_)
        for byte in self.message:
            data.append(byte)

        data.append(util.crc(data))
        data.append(FRAME_END)
        return bytes(data)

    def to_hex(self) -> str:
        """Converts frame to list of hex bytes."""
        return util.to_hex(self.to_bytes())

    def create_message(self) -> bytearray:
        """Creates bytearray message from
        provided data.
        """
        raise NotImplementedError()

    def parse_message(self, message: bytearray) -> None:
        """Parses data from the frame message.

        Keyword arguments:
        message - bytearray message to parse
        """
        raise NotImplementedError()

    def response(self, **args) -> Frame:
        """Returns instance of Frame
        for response to request, if needed.
        """
        raise NotImplementedError()
