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


class HideAllChatJoinRequests(TLObject):  # type: ignore
    """Dismiss or approve all join requests related to a specific chat or channel.


    Details:
        - Layer: ``224``
        - ID: ``E085F4EA``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat or channel

        approved (``bool``, *optional*):
            Whether to dismiss or approve all chat join requests »

        link (``str``, *optional*):
            Only dismiss or approve join requests » initiated using this invite link

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "approved", "link"]

    ID = 0xe085f4ea
    QUALNAME = "functions.messages.HideAllChatJoinRequests"

    def __init__(self, *, peer: "raw.base.InputPeer", approved: Optional[bool] = None, link: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.approved = approved  # flags.0?true
        self.link = link  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HideAllChatJoinRequests":

        flags = Int.read(b)

        approved = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        link = String.read(b) if flags & (1 << 1) else None
        return HideAllChatJoinRequests(peer=peer, approved=approved, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.approved else 0
        flags |= (1 << 1) if self.link is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.link is not None:
            b.write(String(self.link))

        return b.getvalue()
