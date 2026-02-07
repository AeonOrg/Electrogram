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


class FaveSticker(TLObject):  # type: ignore
    """Mark or unmark a sticker as favorite


    Details:
        - Layer: ``224``
        - ID: ``B9FFC55B``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            Sticker in question

        unfave (``bool``):
            Whether to add or remove a sticker from favorites

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unfave"]

    ID = 0xb9ffc55b
    QUALNAME = "functions.messages.FaveSticker"

    def __init__(self, *, id: "raw.base.InputDocument", unfave: bool) -> None:
        self.id = id  # InputDocument
        self.unfave = unfave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FaveSticker":
        # No flags

        id = TLObject.read(b)

        unfave = Bool.read(b)

        return FaveSticker(id=id, unfave=unfave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        b.write(Bool(self.unfave))

        return b.getvalue()
