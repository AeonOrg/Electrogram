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


class ImportCard(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4FE196FE``

    Parameters:
        export_card (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["export_card"]

    ID = 0x4fe196fe
    QUALNAME = "functions.contacts.ImportCard"

    def __init__(self, *, export_card: List[int]) -> None:
        self.export_card = export_card  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportCard":
        # No flags

        export_card = TLObject.read(b, Int)

        return ImportCard(export_card=export_card)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.export_card, Int))

        return b.getvalue()
