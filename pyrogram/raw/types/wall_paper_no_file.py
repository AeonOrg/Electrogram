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


class WallPaperNoFile(TLObject):  # type: ignore
    """Represents a wallpaper only based on colors/gradients.

    Constructor of :obj:`~pyrogram.raw.base.WallPaper`.

    Details:
        - Layer: ``224``
        - ID: ``E0804116``

    Parameters:
        id (``int`` ``64-bit``):
            Wallpaper ID

        default (``bool``, *optional*):
            Whether this is the default wallpaper

        dark (``bool``, *optional*):
            Whether this wallpaper should be used in dark mode.

        settings (:obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`, *optional*):
            Info on how to generate the wallpaper.

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWallPaper
            account.UploadWallPaper
            account.GetMultiWallPapers
    """

    __slots__: List[str] = ["id", "default", "dark", "settings"]

    ID = 0xe0804116
    QUALNAME = "types.WallPaperNoFile"

    def __init__(self, *, id: int, default: Optional[bool] = None, dark: Optional[bool] = None, settings: "raw.base.WallPaperSettings" = None) -> None:
        self.id = id  # long
        self.default = default  # flags.1?true
        self.dark = dark  # flags.4?true
        self.settings = settings  # flags.2?WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaperNoFile":

        id = Long.read(b)

        flags = Int.read(b)

        default = True if flags & (1 << 1) else False
        dark = True if flags & (1 << 4) else False
        settings = TLObject.read(b) if flags & (1 << 2) else None

        return WallPaperNoFile(id=id, default=default, dark=dark, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))


        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 4) if self.dark else 0
        flags |= (1 << 2) if self.settings is not None else 0
        b.write(Int(flags))

        if self.settings is not None:
            b.write(self.settings.write())

        return b.getvalue()
