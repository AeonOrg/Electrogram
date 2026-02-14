from __future__ import annotations

from io import BytesIO
from typing import Any

from .primitives.int import Int, Long
from .tl_object import TLObject


class Message(TLObject):
    ID = 0x5BB8E511  # hex(crc32(b"message msg_id:long seqno:int bytes:int body:Object = Message"))

    __slots__ = ["body", "length", "msg_id", "seq_no"]

    QUALNAME = "Message"

    def __init__(
        self,
        body: TLObject,
        msg_id: int,
        seq_no: int,
        length: int,
    ) -> None:
        self.msg_id = msg_id
        self.seq_no = seq_no
        self.length = length
        self.body = body

    @staticmethod
    def read(data: BytesIO, *args: Any) -> Message:  # noqa: ARG004
        msg_id = Long.read(data)
        seq_no = Int.read(data)
        length = Int.read(data)
        body = data.read(length)

        return Message(TLObject.read(BytesIO(body)), msg_id, seq_no, length)

    def write(self, b: BytesIO | None = None) -> bytes:
        is_top = b is None

        if is_top:
            b = BytesIO()

        Long.write(self.msg_id, b)
        Int.write(self.seq_no, b)
        Int.write(self.length, b)
        self.body.write(b)

        if is_top:
            return b.getvalue()
        return None
