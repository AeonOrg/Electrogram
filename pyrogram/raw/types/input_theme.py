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


class InputTheme(TLObject):  # type: ignore
    """Theme

    Constructor of :obj:`~pyrogram.raw.base.InputTheme`.

    Details:
        - Layer: ``224``
        - ID: ``3C5693E9``

    Parameters:
        id (``int`` ``64-bit``):
            ID

        access_hash (``int`` ``64-bit``):
            Access hash

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0x3c5693e9
    QUALNAME = "types.InputTheme"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputTheme":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        return InputTheme(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
