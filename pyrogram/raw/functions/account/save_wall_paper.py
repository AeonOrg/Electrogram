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


class SaveWallPaper(TLObject):  # type: ignore
    """Install/uninstall wallpaper


    Details:
        - Layer: ``224``
        - ID: ``6C5A5B37``

    Parameters:
        wallpaper (:obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`):
            Wallpaper to install or uninstall

        unsave (``bool``):
            Uninstall wallpaper?

        settings (:obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`):
            Wallpaper settings

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["wallpaper", "unsave", "settings"]

    ID = 0x6c5a5b37
    QUALNAME = "functions.account.SaveWallPaper"

    def __init__(self, *, wallpaper: "raw.base.InputWallPaper", unsave: bool, settings: "raw.base.WallPaperSettings") -> None:
        self.wallpaper = wallpaper  # InputWallPaper
        self.unsave = unsave  # Bool
        self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveWallPaper":
        # No flags

        wallpaper = TLObject.read(b)

        unsave = Bool.read(b)

        settings = TLObject.read(b)

        return SaveWallPaper(wallpaper=wallpaper, unsave=unsave, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.wallpaper.write())

        b.write(Bool(self.unsave))

        b.write(self.settings.write())

        return b.getvalue()
