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


class ReactionCustomEmoji(TLObject):  # type: ignore
    """Custom emoji message reaction

    Constructor of :obj:`~pyrogram.raw.base.Reaction`.

    Details:
        - Layer: ``224``
        - ID: ``8935FC73``

    Parameters:
        document_id (``int`` ``64-bit``):
            Custom emoji document ID

    """

    __slots__: List[str] = ["document_id"]

    ID = 0x8935fc73
    QUALNAME = "types.ReactionCustomEmoji"

    def __init__(self, *, document_id: int) -> None:
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionCustomEmoji":
        # No flags

        document_id = Long.read(b)

        return ReactionCustomEmoji(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.document_id))

        return b.getvalue()
