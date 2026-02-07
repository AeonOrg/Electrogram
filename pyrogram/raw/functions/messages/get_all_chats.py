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


class GetAllChats(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``875F74BE``

    Parameters:
        except_ids (List of ``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["except_ids"]

    ID = 0x875f74be
    QUALNAME = "functions.messages.GetAllChats"

    def __init__(self, *, except_ids: List[int]) -> None:
        self.except_ids = except_ids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllChats":
        # No flags

        except_ids = TLObject.read(b, Long)

        return GetAllChats(except_ids=except_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.except_ids, Long))

        return b.getvalue()
