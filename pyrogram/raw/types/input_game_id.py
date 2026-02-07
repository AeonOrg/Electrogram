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


class InputGameID(TLObject):  # type: ignore
    """Indicates an already sent game

    Constructor of :obj:`~pyrogram.raw.base.InputGame`.

    Details:
        - Layer: ``224``
        - ID: ``32C3E77``

    Parameters:
        id (``int`` ``64-bit``):
            game ID from Game constructor

        access_hash (``int`` ``64-bit``):
            access hash from Game constructor

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0x32c3e77
    QUALNAME = "types.InputGameID"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGameID":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        return InputGameID(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
