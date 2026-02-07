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


class UpdateStickerSets(TLObject):  # type: ignore
    """Installed stickersets have changed, the client should refetch them as described in the docs.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``31C24808``

    Parameters:
        masks (``bool``, *optional*):
            Whether mask stickersets have changed

        emojis (``bool``, *optional*):
            Whether the list of installed custom emoji stickersets has changed

    """

    __slots__: List[str] = ["masks", "emojis"]

    ID = 0x31c24808
    QUALNAME = "types.UpdateStickerSets"

    def __init__(self, *, masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        self.masks = masks  # flags.0?true
        self.emojis = emojis  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStickerSets":

        flags = Int.read(b)

        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        return UpdateStickerSets(masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.emojis else 0
        b.write(Int(flags))

        return b.getvalue()
