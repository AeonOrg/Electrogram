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


class InputBotInlineMessageID(TLObject):  # type: ignore
    """Represents a sent inline message from the perspective of a bot (legacy constructor)

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessageID`.

    Details:
        - Layer: ``224``
        - ID: ``890C3D89``

    Parameters:
        dc_id (``int`` ``32-bit``):
            DC ID to use when working with this inline message

        id (``int`` ``64-bit``):
            ID of message, contains both the (32-bit, legacy) owner ID and the message ID, used only for Bot API backwards compatibility with 32-bit user ID.

        access_hash (``int`` ``64-bit``):
            Access hash of message

    """

    __slots__: List[str] = ["dc_id", "id", "access_hash"]

    ID = 0x890c3d89
    QUALNAME = "types.InputBotInlineMessageID"

    def __init__(self, *, dc_id: int, id: int, access_hash: int) -> None:
        self.dc_id = dc_id  # int
        self.id = id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageID":
        # No flags

        dc_id = Int.read(b)

        id = Long.read(b)

        access_hash = Long.read(b)

        return InputBotInlineMessageID(dc_id=dc_id, id=id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.dc_id))

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        return b.getvalue()
