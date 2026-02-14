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

    @staticmethod
    def read(data: BytesIO, *args: Any) -> MsgContainer:  # noqa: ARG004
        count = Int.read(data)
        return MsgContainer([Message.read(data) for _ in range(count)])

    def write(self, b: BytesIO | None = None) -> bytes:
        is_top = b is None

        if is_top:
            b = BytesIO()

        Int.write(self.ID, b, False)

        count = len(self.messages)
        Int.write(count, b)

        for message in self.messages:
            message.write(b)

        if is_top:
            return b.getvalue()
        return None
