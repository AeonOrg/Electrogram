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


class StarGiftAttributeIdModel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeId`.

    Details:
        - Layer: ``224``
        - ID: ``48AAAE3C``

    Parameters:
        document_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["document_id"]

    ID = 0x48aaae3c
    QUALNAME = "types.StarGiftAttributeIdModel"

    def __init__(self, *, document_id: int) -> None:
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeIdModel":
        # No flags

        document_id = Long.read(b)

        return StarGiftAttributeIdModel(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.document_id))

        return b.getvalue()
