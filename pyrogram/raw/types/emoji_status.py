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


class EmojiStatus(TLObject):  # type: ignore
    """An emoji status

    Constructor of :obj:`~pyrogram.raw.base.EmojiStatus`.

    Details:
        - Layer: ``224``
        - ID: ``E7FF068A``

    Parameters:
        document_id (``int`` ``64-bit``):
            Custom emoji document ID

        until (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["document_id", "until"]

    ID = 0xe7ff068a
    QUALNAME = "types.EmojiStatus"

    def __init__(self, *, document_id: int, until: Optional[int] = None) -> None:
        self.document_id = document_id  # long
        self.until = until  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiStatus":

        flags = Int.read(b)

        document_id = Long.read(b)

        until = Int.read(b) if flags & (1 << 0) else None
        return EmojiStatus(document_id=document_id, until=until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.until is not None else 0
        b.write(Int(flags))

        b.write(Long(self.document_id))

        if self.until is not None:
            b.write(Int(self.until))

        return b.getvalue()
