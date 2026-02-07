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


class MsgsAllInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MsgsAllInfo`.

    Details:
        - Layer: ``224``
        - ID: ``8CC0D131``

    Parameters:
        msg_ids (List of ``int`` ``64-bit``):
            N/A

        info (``str``):
            N/A

    """

    __slots__: List[str] = ["msg_ids", "info"]

    ID = 0x8cc0d131
    QUALNAME = "types.MsgsAllInfo"

    def __init__(self, *, msg_ids: List[int], info: str) -> None:
        self.msg_ids = msg_ids  # Vector<long>
        self.info = info  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MsgsAllInfo":
        # No flags

        msg_ids = TLObject.read(b, Long)

        info = String.read(b)

        return MsgsAllInfo(msg_ids=msg_ids, info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.msg_ids, Long))

        b.write(String(self.info))

        return b.getvalue()
