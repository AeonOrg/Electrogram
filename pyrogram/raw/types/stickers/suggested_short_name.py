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


class SuggestedShortName(TLObject):  # type: ignore
    """A suggested short name for a stickerpack

    Constructor of :obj:`~pyrogram.raw.base.stickers.SuggestedShortName`.

    Details:
        - Layer: ``224``
        - ID: ``85FEA03F``

    Parameters:
        short_name (``str``):
            Suggested short name

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stickers.SuggestShortName
    """

    __slots__: List[str] = ["short_name"]

    ID = 0x85fea03f
    QUALNAME = "types.stickers.SuggestedShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestedShortName":
        # No flags

        short_name = String.read(b)

        return SuggestedShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.short_name))

        return b.getvalue()
