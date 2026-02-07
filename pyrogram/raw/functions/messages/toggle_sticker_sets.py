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


class ToggleStickerSets(TLObject):  # type: ignore
    """Apply changes to multiple stickersets


    Details:
        - Layer: ``224``
        - ID: ``B5052FEA``

    Parameters:
        stickersets (List of :obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Stickersets to act upon

        uninstall (``bool``, *optional*):
            Uninstall the specified stickersets

        archive (``bool``, *optional*):
            Archive the specified stickersets

        unarchive (``bool``, *optional*):
            Unarchive the specified stickersets

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stickersets", "uninstall", "archive", "unarchive"]

    ID = 0xb5052fea
    QUALNAME = "functions.messages.ToggleStickerSets"

    def __init__(self, *, stickersets: List["raw.base.InputStickerSet"], uninstall: Optional[bool] = None, archive: Optional[bool] = None, unarchive: Optional[bool] = None) -> None:
        self.stickersets = stickersets  # Vector<InputStickerSet>
        self.uninstall = uninstall  # flags.0?true
        self.archive = archive  # flags.1?true
        self.unarchive = unarchive  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleStickerSets":

        flags = Int.read(b)

        uninstall = True if flags & (1 << 0) else False
        archive = True if flags & (1 << 1) else False
        unarchive = True if flags & (1 << 2) else False
        stickersets = TLObject.read(b)

        return ToggleStickerSets(stickersets=stickersets, uninstall=uninstall, archive=archive, unarchive=unarchive)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.uninstall else 0
        flags |= (1 << 1) if self.archive else 0
        flags |= (1 << 2) if self.unarchive else 0
        b.write(Int(flags))

        b.write(Vector(self.stickersets))

        return b.getvalue()
