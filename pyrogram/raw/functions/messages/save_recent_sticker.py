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


class SaveRecentSticker(TLObject):  # type: ignore
    """Add/remove sticker from recent stickers list


    Details:
        - Layer: ``224``
        - ID: ``392718F8``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            Sticker

        unsave (``bool``):
            Whether to save or unsave the sticker

        attached (``bool``, *optional*):
            Whether to add/remove stickers recently attached to photo or video files

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unsave", "attached"]

    ID = 0x392718f8
    QUALNAME = "functions.messages.SaveRecentSticker"

    def __init__(self, *, id: "raw.base.InputDocument", unsave: bool, attached: Optional[bool] = None) -> None:
        self.id = id  # InputDocument
        self.unsave = unsave  # Bool
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveRecentSticker":

        flags = Int.read(b)

        attached = True if flags & (1 << 0) else False
        id = TLObject.read(b)

        unsave = Bool.read(b)

        return SaveRecentSticker(id=id, unsave=unsave, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))

        b.write(self.id.write())

        b.write(Bool(self.unsave))

        return b.getvalue()
