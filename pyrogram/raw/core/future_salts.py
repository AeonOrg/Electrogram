from __future__ import annotations

from io import BytesIO
from typing import Any

from .future_salt import FutureSalt
from .primitives.int import Int, Long
from .tl_object import TLObject


class FutureSalts(TLObject):
    ID = 0xAE500895

    __slots__ = ["now", "req_msg_id", "salts"]

    QUALNAME = "FutureSalts"

    def __init__(self, req_msg_id: int, now: int, salts: list[FutureSalt]) -> None:
        self.req_msg_id = req_msg_id
        self.now = now
        self.salts = salts

    @staticmethod
    def read(data: BytesIO, *args: Any) -> FutureSalts:  # noqa: ARG004
        req_msg_id = Long.read(data)
        now = Int.read(data)

        count = Int.read(data)
        salts = [FutureSalt.read(data) for _ in range(count)]

        return FutureSalts(req_msg_id, now, salts)

    def write(self, b: BytesIO = None) -> bytes:
        is_top = b is None

        if is_top:
            b = BytesIO()

        Int.write(self.ID, b, False)

        Long.write(self.req_msg_id, b)
        Int.write(self.now, b)

        count = len(self.salts)
        Int.write(count, b)

        for salt in self.salts:
            salt.write(b)

        if is_top:
            return b.getvalue()
