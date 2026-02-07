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


class Themes(TLObject):  # type: ignore
    """Installed themes

    Constructor of :obj:`~pyrogram.raw.base.account.Themes`.

    Details:
        - Layer: ``224``
        - ID: ``9A3D8C6D``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        themes (List of :obj:`Theme <pyrogram.raw.base.Theme>`):
            Themes

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetThemes
            account.GetChatThemes
    """

    __slots__: List[str] = ["hash", "themes"]

    ID = 0x9a3d8c6d
    QUALNAME = "types.account.Themes"

    def __init__(self, *, hash: int, themes: List["raw.base.Theme"]) -> None:
        self.hash = hash  # long
        self.themes = themes  # Vector<Theme>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Themes":
        # No flags

        hash = Long.read(b)

        themes = TLObject.read(b)

        return Themes(hash=hash, themes=themes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.themes))

        return b.getvalue()
