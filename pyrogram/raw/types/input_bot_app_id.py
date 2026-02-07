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


class InputBotAppID(TLObject):  # type: ignore
    """Used to fetch information about a direct link Mini App by its ID

    Constructor of :obj:`~pyrogram.raw.base.InputBotApp`.

    Details:
        - Layer: ``224``
        - ID: ``A920BD7A``

    Parameters:
        id (``int`` ``64-bit``):
            direct link Mini App ID.

        access_hash (``int`` ``64-bit``):
            Access hash, obtained from the botApp constructor.

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0xa920bd7a
    QUALNAME = "types.InputBotAppID"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotAppID":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        return InputBotAppID(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
