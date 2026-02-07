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


class SuggestShortName(TLObject):  # type: ignore
    """Suggests a short name for a given stickerpack name


    Details:
        - Layer: ``224``
        - ID: ``4DAFC503``

    Parameters:
        title (``str``):
            Sticker pack name

    Returns:
        :obj:`stickers.SuggestedShortName <pyrogram.raw.base.stickers.SuggestedShortName>`
    """

    __slots__: List[str] = ["title"]

    ID = 0x4dafc503
    QUALNAME = "functions.stickers.SuggestShortName"

    def __init__(self, *, title: str) -> None:
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestShortName":
        # No flags

        title = String.read(b)

        return SuggestShortName(title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        return b.getvalue()
