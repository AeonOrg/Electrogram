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


class UpdateContactNote(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``139F63FB``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "note"]

    ID = 0x139f63fb
    QUALNAME = "functions.contacts.UpdateContactNote"

    def __init__(self, *, id: "raw.base.InputUser", note: "raw.base.TextWithEntities") -> None:
        self.id = id  # InputUser
        self.note = note  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateContactNote":
        # No flags

        id = TLObject.read(b)

        note = TLObject.read(b)

        return UpdateContactNote(id=id, note=note)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        b.write(self.note.write())

        return b.getvalue()
