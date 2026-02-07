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


class UpdateMessageID(TLObject):  # type: ignore
    """Sent message with random_id client identifier was assigned an identifier.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``4E90BFD6``

    Parameters:
        id (``int`` ``32-bit``):
            id identifier of a respective Message

        random_id (``int`` ``64-bit``):
            Previously transferred client random_id identifier

    """

    __slots__: List[str] = ["id", "random_id"]

    ID = 0x4e90bfd6
    QUALNAME = "types.UpdateMessageID"

    def __init__(self, *, id: int, random_id: int) -> None:
        self.id = id  # int
        self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageID":
        # No flags

        id = Int.read(b)

        random_id = Long.read(b)

        return UpdateMessageID(id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.id))

        b.write(Long(self.random_id))

        return b.getvalue()
