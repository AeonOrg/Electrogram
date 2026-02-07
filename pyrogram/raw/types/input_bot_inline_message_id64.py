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


class InputBotInlineMessageID64(TLObject):  # type: ignore
    """Represents a sent inline message from the perspective of a bot

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessageID`.

    Details:
        - Layer: ``224``
        - ID: ``B6D915D7``

    Parameters:
        dc_id (``int`` ``32-bit``):
            DC ID to use when working with this inline message

        owner_id (``int`` ``64-bit``):
            ID of the owner of this message

        id (``int`` ``32-bit``):
            ID of message

        access_hash (``int`` ``64-bit``):
            Access hash of message

    """

    __slots__: List[str] = ["dc_id", "owner_id", "id", "access_hash"]

    ID = 0xb6d915d7
    QUALNAME = "types.InputBotInlineMessageID64"

    def __init__(self, *, dc_id: int, owner_id: int, id: int, access_hash: int) -> None:
        self.dc_id = dc_id  # int
        self.owner_id = owner_id  # long
        self.id = id  # int
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageID64":
        # No flags

        dc_id = Int.read(b)

        owner_id = Long.read(b)

        id = Int.read(b)

        access_hash = Long.read(b)

        return InputBotInlineMessageID64(dc_id=dc_id, owner_id=owner_id, id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.dc_id))

        b.write(Long(self.owner_id))

        b.write(Int(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
