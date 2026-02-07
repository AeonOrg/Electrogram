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


class EditExportedInvite(TLObject):  # type: ignore
    """Edit a chat folder deep link ».


    Details:
        - Layer: ``224``
        - ID: ``653DB63D``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            Folder ID

        slug (``str``):
            slug obtained from the chat folder deep link ».

        revoked (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            If set, sets a new name for the link

        peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            If set, changes the list of peers shared with the link

    Returns:
        :obj:`ExportedChatlistInvite <pyrogram.raw.base.ExportedChatlistInvite>`
    """

    __slots__: List[str] = ["chatlist", "slug", "revoked", "title", "peers"]

    ID = 0x653db63d
    QUALNAME = "functions.chatlists.EditExportedInvite"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", slug: str, revoked: Optional[bool] = None, title: Optional[str] = None, peers: Optional[List["raw.base.InputPeer"]] = None) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.slug = slug  # string
        self.revoked = revoked  # flags.0?true
        self.title = title  # flags.1?string
        self.peers = peers  # flags.2?Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditExportedInvite":

        flags = Int.read(b)

        revoked = True if flags & (1 << 0) else False
        chatlist = TLObject.read(b)

        slug = String.read(b)

        title = String.read(b) if flags & (1 << 1) else None
        peers = TLObject.read(b) if flags & (1 << 2) else []

        return EditExportedInvite(chatlist=chatlist, slug=slug, revoked=revoked, title=title, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.peers else 0
        b.write(Int(flags))

        b.write(self.chatlist.write())

        b.write(String(self.slug))

        if self.title is not None:
            b.write(String(self.title))

        if self.peers is not None:
            b.write(Vector(self.peers))

        return b.getvalue()
