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


class GetExportedChatInvite(TLObject):  # type: ignore
    """Get info about a chat invite


    Details:
        - Layer: ``224``
        - ID: ``73746F5C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chat

        link (``str``):
            Invite link

    Returns:
        :obj:`messages.ExportedChatInvite <pyrogram.raw.base.messages.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "link"]

    ID = 0x73746f5c
    QUALNAME = "functions.messages.GetExportedChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str) -> None:
        self.peer = peer  # InputPeer
        self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetExportedChatInvite":
        # No flags

        peer = TLObject.read(b)

        link = String.read(b)

        return GetExportedChatInvite(peer=peer, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(String(self.link))

        return b.getvalue()
