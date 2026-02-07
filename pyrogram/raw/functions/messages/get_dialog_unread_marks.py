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


class GetDialogUnreadMarks(TLObject):  # type: ignore
    """Get dialogs manually marked as unread


    Details:
        - Layer: ``224``
        - ID: ``21202222``

    Parameters:
        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        List of :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`
    """

    __slots__: List[str] = ["parent_peer"]

    ID = 0x21202222
    QUALNAME = "functions.messages.GetDialogUnreadMarks"

    def __init__(self, *, parent_peer: "raw.base.InputPeer" = None) -> None:
        self.parent_peer = parent_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogUnreadMarks":

        flags = Int.read(b)

        parent_peer = TLObject.read(b) if flags & (1 << 0) else None

        return GetDialogUnreadMarks(parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.parent_peer is not None else 0
        b.write(Int(flags))

        if self.parent_peer is not None:
            b.write(self.parent_peer.write())

        return b.getvalue()
