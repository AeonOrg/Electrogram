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


class SavedMusic(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.users.SavedMusic`.

    Details:
        - Layer: ``224``
        - ID: ``34A2F297``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        documents (List of :obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetSavedMusic
            users.GetSavedMusicByID
    """

    __slots__: List[str] = ["count", "documents"]

    ID = 0x34a2f297
    QUALNAME = "types.users.SavedMusic"

    def __init__(self, *, count: int, documents: List["raw.base.Document"]) -> None:
        self.count = count  # int
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedMusic":
        # No flags

        count = Int.read(b)

        documents = TLObject.read(b)

        return SavedMusic(count=count, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Vector(self.documents))

        return b.getvalue()
