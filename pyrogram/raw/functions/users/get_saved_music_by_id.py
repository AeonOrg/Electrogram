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


class GetSavedMusicByID(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7573A4E9``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        documents (List of :obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

    Returns:
        :obj:`users.SavedMusic <pyrogram.raw.base.users.SavedMusic>`
    """

    __slots__: List[str] = ["id", "documents"]

    ID = 0x7573a4e9
    QUALNAME = "functions.users.GetSavedMusicByID"

    def __init__(self, *, id: "raw.base.InputUser", documents: List["raw.base.InputDocument"]) -> None:
        self.id = id  # InputUser
        self.documents = documents  # Vector<InputDocument>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedMusicByID":
        # No flags

        id = TLObject.read(b)

        documents = TLObject.read(b)

        return GetSavedMusicByID(id=id, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        b.write(Vector(self.documents))

        return b.getvalue()
