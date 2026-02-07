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


class MessageActionChangeCreator(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``E188503B``

    Parameters:
        new_creator_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["new_creator_id"]

    ID = 0xe188503b
    QUALNAME = "types.MessageActionChangeCreator"

    def __init__(self, *, new_creator_id: int) -> None:
        self.new_creator_id = new_creator_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChangeCreator":
        # No flags

        new_creator_id = Long.read(b)

        return MessageActionChangeCreator(new_creator_id=new_creator_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.new_creator_id))

        return b.getvalue()
