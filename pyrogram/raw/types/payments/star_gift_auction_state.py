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


class StarGiftAuctionState(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftAuctionState`.

    Details:
        - Layer: ``224``
        - ID: ``6B39F4EC``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        state (:obj:`StarGiftAuctionState <pyrogram.raw.base.StarGiftAuctionState>`):
            N/A

        user_state (:obj:`StarGiftAuctionUserState <pyrogram.raw.base.StarGiftAuctionUserState>`):
            N/A

        timeout (``int`` ``32-bit``):
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

            payments.GetStarGiftAuctionState
    """

    __slots__: List[str] = ["gift", "state", "user_state", "timeout", "users", "chats"]

    ID = 0x6b39f4ec
    QUALNAME = "types.payments.StarGiftAuctionState"

    def __init__(self, *, gift: "raw.base.StarGift", state: "raw.base.StarGiftAuctionState", user_state: "raw.base.StarGiftAuctionUserState", timeout: int, users: List["raw.base.User"], chats: List["raw.base.Chat"]) -> None:
        self.gift = gift  # StarGift
        self.state = state  # StarGiftAuctionState
        self.user_state = user_state  # StarGiftAuctionUserState
        self.timeout = timeout  # int
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionState":
        # No flags

        gift = TLObject.read(b)

        state = TLObject.read(b)

        user_state = TLObject.read(b)

        timeout = Int.read(b)

        users = TLObject.read(b)

        chats = TLObject.read(b)

        return StarGiftAuctionState(gift=gift, state=state, user_state=user_state, timeout=timeout, users=users, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.gift.write())

        b.write(self.state.write())

        b.write(self.user_state.write())

        b.write(Int(self.timeout))

        b.write(Vector(self.users))

        b.write(Vector(self.chats))

        return b.getvalue()
