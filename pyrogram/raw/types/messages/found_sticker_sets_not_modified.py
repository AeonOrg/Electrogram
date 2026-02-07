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


class FoundStickerSetsNotModified(TLObject):  # type: ignore
    """No further results were found

    Constructor of :obj:`~pyrogram.raw.base.messages.FoundStickerSets`.

    Details:
        - Layer: ``224``
        - ID: ``D54B65D``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SearchStickerSets
            messages.SearchEmojiStickerSets
    """

    __slots__: List[str] = []

    ID = 0xd54b65d
    QUALNAME = "types.messages.FoundStickerSetsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FoundStickerSetsNotModified":
        # No flags

        return FoundStickerSetsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
