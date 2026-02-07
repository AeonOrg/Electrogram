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


class EmojiGroups(TLObject):  # type: ignore
    """Represents a list of emoji categories.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGroups`.

    Details:
        - Layer: ``224``
        - ID: ``881FB94B``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        groups (List of :obj:`EmojiGroup <pyrogram.raw.base.EmojiGroup>`):
            A list of emoji categories.

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGroups
            messages.GetEmojiStatusGroups
            messages.GetEmojiProfilePhotoGroups
            messages.GetEmojiStickerGroups
    """

    __slots__: List[str] = ["hash", "groups"]

    ID = 0x881fb94b
    QUALNAME = "types.messages.EmojiGroups"

    def __init__(self, *, hash: int, groups: List["raw.base.EmojiGroup"]) -> None:
        self.hash = hash  # int
        self.groups = groups  # Vector<EmojiGroup>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroups":
        # No flags

        hash = Int.read(b)

        groups = TLObject.read(b)

        return EmojiGroups(hash=hash, groups=groups)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(Vector(self.groups))

        return b.getvalue()
