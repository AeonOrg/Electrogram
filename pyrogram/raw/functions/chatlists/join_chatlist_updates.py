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


class JoinChatlistUpdates(TLObject):  # type: ignore
    """Join channels and supergroups recently added to a chat folder deep link ».


    Details:
        - Layer: ``224``
        - ID: ``E089F8F5``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            The folder

        peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            List of new chats to join, fetched using chatlists.getChatlistUpdates and filtered as specified in the documentation ».

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chatlist", "peers"]

    ID = 0xe089f8f5
    QUALNAME = "functions.chatlists.JoinChatlistUpdates"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", peers: List["raw.base.InputPeer"]) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.peers = peers  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinChatlistUpdates":
        # No flags

        chatlist = TLObject.read(b)

        peers = TLObject.read(b)

        return JoinChatlistUpdates(chatlist=chatlist, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.chatlist.write())

        b.write(Vector(self.peers))

        return b.getvalue()
