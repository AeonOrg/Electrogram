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


class StickerSetNotModified(TLObject):  # type: ignore
    """The stickerset hasn't changed

    Constructor of :obj:`~pyrogram.raw.base.messages.StickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``D3F924EB``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetStickerSet
            stickers.CreateStickerSet
            stickers.RemoveStickerFromSet
            stickers.ChangeStickerPosition
            stickers.AddStickerToSet
            stickers.SetStickerSetThumb
            stickers.ChangeSticker
            stickers.RenameStickerSet
            stickers.ReplaceSticker
    """

    __slots__: List[str] = []

    ID = 0xd3f924eb
    QUALNAME = "types.messages.StickerSetNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetNotModified":
        # No flags

        return StickerSetNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
