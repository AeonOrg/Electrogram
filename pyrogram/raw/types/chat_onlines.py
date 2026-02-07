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


class ChatOnlines(TLObject):  # type: ignore
    """Number of online users in a chat

    Constructor of :obj:`~pyrogram.raw.base.ChatOnlines`.

    Details:
        - Layer: ``224``
        - ID: ``F041E250``

    Parameters:
        onlines (``int`` ``32-bit``):
            Number of online users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetOnlines
    """

    __slots__: List[str] = ["onlines"]

    ID = 0xf041e250
    QUALNAME = "types.ChatOnlines"

    def __init__(self, *, onlines: int) -> None:
        self.onlines = onlines  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatOnlines":
        # No flags

        onlines = Int.read(b)

        return ChatOnlines(onlines=onlines)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.onlines))

        return b.getvalue()
