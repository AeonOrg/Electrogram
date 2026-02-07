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


class StarGifts(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGifts`.

    Details:
        - Layer: ``224``
        - ID: ``2ED82995``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        gifts (List of :obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGifts
    """

    __slots__: List[str] = ["hash", "gifts", "chats", "users"]

    ID = 0x2ed82995
    QUALNAME = "types.payments.StarGifts"

    def __init__(self, *, hash: int, gifts: List["raw.base.StarGift"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.hash = hash  # int
        self.gifts = gifts  # Vector<StarGift>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGifts":
        # No flags

        hash = Int.read(b)

        gifts = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return StarGifts(hash=hash, gifts=gifts, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(Vector(self.gifts))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
