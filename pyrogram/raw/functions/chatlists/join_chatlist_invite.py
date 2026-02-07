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


class JoinChatlistInvite(TLObject):  # type: ignore
    """Import a chat folder deep link », joining some or all the chats in the folder.


    Details:
        - Layer: ``224``
        - ID: ``A6B1E39A``

    Parameters:
        slug (``str``):
            slug obtained from a chat folder deep link ».

        peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            List of new chats to join, fetched using chatlists.checkChatlistInvite and filtered as specified in the documentation ».

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["slug", "peers"]

    ID = 0xa6b1e39a
    QUALNAME = "functions.chatlists.JoinChatlistInvite"

    def __init__(self, *, slug: str, peers: List["raw.base.InputPeer"]) -> None:
        self.slug = slug  # string
        self.peers = peers  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinChatlistInvite":
        # No flags

        slug = String.read(b)

        peers = TLObject.read(b)

        return JoinChatlistInvite(slug=slug, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        b.write(Vector(self.peers))

        return b.getvalue()
