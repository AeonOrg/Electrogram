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


class UpdateStickerSetsOrder(TLObject):  # type: ignore
    """The order of stickersets was changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``BB2D201``

    Parameters:
        order (List of ``int`` ``64-bit``):
            New sticker order by sticker ID

        masks (``bool``, *optional*):
            Whether the updated stickers are mask stickers

        emojis (``bool``, *optional*):
            Whether the updated stickers are custom emoji stickers

    """

    __slots__: List[str] = ["order", "masks", "emojis"]

    ID = 0xbb2d201
    QUALNAME = "types.UpdateStickerSetsOrder"

    def __init__(self, *, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        self.order = order  # Vector<long>
        self.masks = masks  # flags.0?true
        self.emojis = emojis  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStickerSetsOrder":

        flags = Int.read(b)

        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        order = TLObject.read(b, Long)

        return UpdateStickerSetsOrder(order=order, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.emojis else 0
        b.write(Int(flags))

        b.write(Vector(self.order, Long))

        return b.getvalue()
