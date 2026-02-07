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


class DialogFolder(TLObject):  # type: ignore
    """Dialog in folder

    Constructor of :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``224``
        - ID: ``71BD134C``

    Parameters:
        folder (:obj:`Folder <pyrogram.raw.base.Folder>`):
            The folder

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer in folder

        top_message (``int`` ``32-bit``):
            Latest message ID of dialog

        unread_muted_peers_count (``int`` ``32-bit``):
            Number of unread muted peers in folder

        unread_unmuted_peers_count (``int`` ``32-bit``):
            Number of unread unmuted peers in folder

        unread_muted_messages_count (``int`` ``32-bit``):
            Number of unread messages from muted peers in folder

        unread_unmuted_messages_count (``int`` ``32-bit``):
            Number of unread messages from unmuted peers in folder

        pinned (``bool``, *optional*):
            Is this folder pinned

    """

    __slots__: List[str] = ["folder", "peer", "top_message", "unread_muted_peers_count", "unread_unmuted_peers_count", "unread_muted_messages_count", "unread_unmuted_messages_count", "pinned"]

    ID = 0x71bd134c
    QUALNAME = "types.DialogFolder"

    def __init__(self, *, folder: "raw.base.Folder", peer: "raw.base.Peer", top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: Optional[bool] = None) -> None:
        self.folder = folder  # Folder
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.unread_muted_peers_count = unread_muted_peers_count  # int
        self.unread_unmuted_peers_count = unread_unmuted_peers_count  # int
        self.unread_muted_messages_count = unread_muted_messages_count  # int
        self.unread_unmuted_messages_count = unread_unmuted_messages_count  # int
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFolder":

        flags = Int.read(b)

        pinned = True if flags & (1 << 2) else False
        folder = TLObject.read(b)

        peer = TLObject.read(b)

        top_message = Int.read(b)

        unread_muted_peers_count = Int.read(b)

        unread_unmuted_peers_count = Int.read(b)

        unread_muted_messages_count = Int.read(b)

        unread_unmuted_messages_count = Int.read(b)

        return DialogFolder(folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))

        b.write(self.folder.write())

        b.write(self.peer.write())

        b.write(Int(self.top_message))

        b.write(Int(self.unread_muted_peers_count))

        b.write(Int(self.unread_unmuted_peers_count))

        b.write(Int(self.unread_muted_messages_count))

        b.write(Int(self.unread_unmuted_messages_count))

        return b.getvalue()
