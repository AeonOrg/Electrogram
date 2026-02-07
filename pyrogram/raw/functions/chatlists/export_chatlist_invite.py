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


class ExportChatlistInvite(TLObject):  # type: ignore
    """Export a folder », creating a chat folder deep link ».


    Details:
        - Layer: ``224``
        - ID: ``8472478E``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            The folder to export

        title (``str``):
            An optional name for the link

        peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The list of channels, group and supergroups to share with the link. Basic groups will automatically be converted to supergroups when invoking the method.

    Returns:
        :obj:`chatlists.ExportedChatlistInvite <pyrogram.raw.base.chatlists.ExportedChatlistInvite>`
    """

    __slots__: List[str] = ["chatlist", "title", "peers"]

    ID = 0x8472478e
    QUALNAME = "functions.chatlists.ExportChatlistInvite"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", title: str, peers: List["raw.base.InputPeer"]) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.title = title  # string
        self.peers = peers  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportChatlistInvite":
        # No flags

        chatlist = TLObject.read(b)

        title = String.read(b)

        peers = TLObject.read(b)

        return ExportChatlistInvite(chatlist=chatlist, title=title, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.chatlist.write())

        b.write(String(self.title))

        b.write(Vector(self.peers))

        return b.getvalue()
