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


class EditChatDefaultBannedRights(TLObject):  # type: ignore
    """Edit the default banned rights of a channel/supergroup/group.


    Details:
        - Layer: ``224``
        - ID: ``A5866B41``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            The new global rights

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "banned_rights"]

    ID = 0xa5866b41
    QUALNAME = "functions.messages.EditChatDefaultBannedRights"

    def __init__(self, *, peer: "raw.base.InputPeer", banned_rights: "raw.base.ChatBannedRights") -> None:
        self.peer = peer  # InputPeer
        self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatDefaultBannedRights":
        # No flags

        peer = TLObject.read(b)

        banned_rights = TLObject.read(b)

        return EditChatDefaultBannedRights(peer=peer, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.banned_rights.write())

        return b.getvalue()
