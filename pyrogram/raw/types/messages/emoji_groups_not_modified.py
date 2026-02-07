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


class EmojiGroupsNotModified(TLObject):  # type: ignore
    """The list of emoji categories hasn't changed.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGroups`.

    Details:
        - Layer: ``224``
        - ID: ``6FB4AD87``

    Parameters:
        No parameters required.

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

    __slots__: List[str] = []

    ID = 0x6fb4ad87
    QUALNAME = "types.messages.EmojiGroupsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroupsNotModified":
        # No flags

        return EmojiGroupsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
