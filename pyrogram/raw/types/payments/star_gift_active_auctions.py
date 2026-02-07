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


class StarGiftActiveAuctions(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftActiveAuctions`.

    Details:
        - Layer: ``224``
        - ID: ``AEF6ABBC``

    Parameters:
        auctions (List of :obj:`StarGiftActiveAuctionState <pyrogram.raw.base.StarGiftActiveAuctionState>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftActiveAuctions
    """

    __slots__: List[str] = ["auctions", "users", "chats"]

    ID = 0xaef6abbc
    QUALNAME = "types.payments.StarGiftActiveAuctions"

    def __init__(self, *, auctions: List["raw.base.StarGiftActiveAuctionState"], users: List["raw.base.User"], chats: List["raw.base.Chat"]) -> None:
        self.auctions = auctions  # Vector<StarGiftActiveAuctionState>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftActiveAuctions":
        # No flags

        auctions = TLObject.read(b)

        users = TLObject.read(b)

        chats = TLObject.read(b)

        return StarGiftActiveAuctions(auctions=auctions, users=users, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.auctions))

        b.write(Vector(self.users))

        b.write(Vector(self.chats))

        return b.getvalue()
