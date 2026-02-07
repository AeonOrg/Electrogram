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


class GetExportedChatInvites(TLObject):  # type: ignore
    """Get info about the chat invites of a specific chat


    Details:
        - Layer: ``224``
        - ID: ``A2B5A3F6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chat

        admin_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Whether to only fetch chat invites from this admin

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        revoked (``bool``, *optional*):
            Whether to fetch revoked chat invites

        offset_date (``int`` ``32-bit``, *optional*):
            Offsets for pagination, for more info click here

        offset_link (``str``, *optional*):
            Offsets for pagination, for more info click here

    Returns:
        :obj:`messages.ExportedChatInvites <pyrogram.raw.base.messages.ExportedChatInvites>`
    """

    __slots__: List[str] = ["peer", "admin_id", "limit", "revoked", "offset_date", "offset_link"]

    ID = 0xa2b5a3f6
    QUALNAME = "functions.messages.GetExportedChatInvites"

    def __init__(self, *, peer: "raw.base.InputPeer", admin_id: "raw.base.InputUser", limit: int, revoked: Optional[bool] = None, offset_date: Optional[int] = None, offset_link: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.admin_id = admin_id  # InputUser
        self.limit = limit  # int
        self.revoked = revoked  # flags.3?true
        self.offset_date = offset_date  # flags.2?int
        self.offset_link = offset_link  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetExportedChatInvites":

        flags = Int.read(b)

        revoked = True if flags & (1 << 3) else False
        peer = TLObject.read(b)

        admin_id = TLObject.read(b)

        offset_date = Int.read(b) if flags & (1 << 2) else None
        offset_link = String.read(b) if flags & (1 << 2) else None
        limit = Int.read(b)

        return GetExportedChatInvites(peer=peer, admin_id=admin_id, limit=limit, revoked=revoked, offset_date=offset_date, offset_link=offset_link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.revoked else 0
        flags |= (1 << 2) if self.offset_date is not None else 0
        flags |= (1 << 2) if self.offset_link is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(self.admin_id.write())

        if self.offset_date is not None:
            b.write(Int(self.offset_date))

        if self.offset_link is not None:
            b.write(String(self.offset_link))

        b.write(Int(self.limit))

        return b.getvalue()
