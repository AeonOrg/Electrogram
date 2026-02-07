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


class InputGroupCall(TLObject):  # type: ignore
    """Points to a specific group call

    Constructor of :obj:`~pyrogram.raw.base.InputGroupCall`.

    Details:
        - Layer: ``224``
        - ID: ``D8AA840F``

    Parameters:
        id (``int`` ``64-bit``):
            Group call ID

        access_hash (``int`` ``64-bit``):
            Group call access hash

    """

    __slots__: List[str] = ["id", "access_hash"]

    ID = 0xd8aa840f
    QUALNAME = "types.InputGroupCall"

    def __init__(self, *, id: int, access_hash: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGroupCall":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        return InputGroupCall(id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
