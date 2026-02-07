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


class UpdateDialogUnreadMark(TLObject):  # type: ignore
    """The manual unread mark of a chat was changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B658F23E``

    Parameters:
        peer (:obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`):
            The dialog

        unread (``bool``, *optional*):
            Was the chat marked or unmarked as read

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "unread", "saved_peer_id"]

    ID = 0xb658f23e
    QUALNAME = "types.UpdateDialogUnreadMark"

    def __init__(self, *, peer: "raw.base.DialogPeer", unread: Optional[bool] = None, saved_peer_id: "raw.base.Peer" = None) -> None:
        self.peer = peer  # DialogPeer
        self.unread = unread  # flags.0?true
        self.saved_peer_id = saved_peer_id  # flags.1?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogUnreadMark":

        flags = Int.read(b)

        unread = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        saved_peer_id = TLObject.read(b) if flags & (1 << 1) else None

        return UpdateDialogUnreadMark(peer=peer, unread=unread, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread else 0
        flags |= (1 << 1) if self.saved_peer_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        return b.getvalue()
