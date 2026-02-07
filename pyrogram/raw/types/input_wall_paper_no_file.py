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


class InputWallPaperNoFile(TLObject):  # type: ignore
    """Wallpaper with no file access hash, used for example when deleting (unsave=true) wallpapers using account.saveWallPaper, specifying just the wallpaper ID.

    Constructor of :obj:`~pyrogram.raw.base.InputWallPaper`.

    Details:
        - Layer: ``224``
        - ID: ``967A462E``

    Parameters:
        id (``int`` ``64-bit``):
            Wallpaper ID

    """

    __slots__: List[str] = ["id"]

    ID = 0x967a462e
    QUALNAME = "types.InputWallPaperNoFile"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWallPaperNoFile":
        # No flags

        id = Long.read(b)

        return InputWallPaperNoFile(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        return b.getvalue()
