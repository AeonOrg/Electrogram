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


class SaveGif(TLObject):  # type: ignore
    """Add GIF to saved gifs list


    Details:
        - Layer: ``224``
        - ID: ``327A30CB``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            GIF to save

        unsave (``bool``):
            Whether to remove GIF from saved gifs list

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unsave"]

    ID = 0x327a30cb
    QUALNAME = "functions.messages.SaveGif"

    def __init__(self, *, id: "raw.base.InputDocument", unsave: bool) -> None:
        self.id = id  # InputDocument
        self.unsave = unsave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveGif":
        # No flags

        id = TLObject.read(b)

        unsave = Bool.read(b)

        return SaveGif(id=id, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        b.write(Bool(self.unsave))

        return b.getvalue()
