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


class GetSendAs(TLObject):  # type: ignore
    """Obtains a list of peers that can be used to send messages in a specific group


    Details:
        - Layer: ``224``
        - ID: ``E785A43F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The group where we intend to send messages

        for_paid_reactions (``bool``, *optional*):
            N/A

        for_live_stories (``bool``, *optional*):
            N/A

    Returns:
        :obj:`channels.SendAsPeers <pyrogram.raw.base.channels.SendAsPeers>`
    """

    __slots__: List[str] = ["peer", "for_paid_reactions", "for_live_stories"]

    ID = 0xe785a43f
    QUALNAME = "functions.channels.GetSendAs"

    def __init__(self, *, peer: "raw.base.InputPeer", for_paid_reactions: Optional[bool] = None, for_live_stories: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.for_paid_reactions = for_paid_reactions  # flags.0?true
        self.for_live_stories = for_live_stories  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSendAs":

        flags = Int.read(b)

        for_paid_reactions = True if flags & (1 << 0) else False
        for_live_stories = True if flags & (1 << 1) else False
        peer = TLObject.read(b)

        return GetSendAs(peer=peer, for_paid_reactions=for_paid_reactions, for_live_stories=for_live_stories)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.for_paid_reactions else 0
        flags |= (1 << 1) if self.for_live_stories else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        return b.getvalue()
