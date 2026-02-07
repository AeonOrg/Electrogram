from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MsgNewDetailedInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MsgDetailedInfo`.

    Details:
        - Layer: ``224``
        - ID: ``809DB6DF``

    Parameters:
        answer_msg_id (``int`` ``64-bit``):
            N/A

        bytes (``int`` ``32-bit``):
            N/A

        status (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["answer_msg_id", "bytes", "status"]

    ID = 0x809db6df
    QUALNAME = "types.MsgNewDetailedInfo"

    def __init__(self, *, answer_msg_id: int, bytes: int, status: int) -> None:
        self.answer_msg_id = answer_msg_id  # long
        self.bytes = bytes  # int
        self.status = status  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MsgNewDetailedInfo":
        # No flags

        answer_msg_id = Long.read(b)

        bytes = Int.read(b)

        status = Int.read(b)

        return MsgNewDetailedInfo(answer_msg_id=answer_msg_id, bytes=bytes, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.answer_msg_id))

        b.write(Int(self.bytes))

        b.write(Int(self.status))

        return b.getvalue()
