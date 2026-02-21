from __future__ import annotations

from io import BytesIO
from typing import Any

from .message import Message
from .primitives.int import Int
from .tl_object import TLObject


class MsgContainer(TLObject):
    ID = 0x73F1F8DC

    __slots__ = ["messages"]

    QUALNAME = "MsgContainer"

    def __init__(self, messages: list[Message]) -> None:
        self.messages = messages

    @classmethod
    def read(cls, b: BytesIO, *args: Any) -> Any:
        count = Int.read(b)
        return MsgContainer([Message.read(b) for _ in range(count)])

    def write(self, *args: Any) -> bytes:  # noqa: ARG002
        b = BytesIO()

        b.write(Int(self.ID, False))

        count = len(self.messages)
        b.write(Int(count))

        for message in self.messages:
            b.write(message.write())

        return b.getvalue()
