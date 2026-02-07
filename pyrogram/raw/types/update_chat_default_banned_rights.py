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


class UpdateChatDefaultBannedRights(TLObject):  # type: ignore
    """Default banned rights in a normal chat were updated

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``54C01850``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The chat

        default_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            New default banned rights

        version (``int`` ``32-bit``):
            Version

    """

    __slots__: List[str] = ["peer", "default_banned_rights", "version"]

    ID = 0x54c01850
    QUALNAME = "types.UpdateChatDefaultBannedRights"

    def __init__(self, *, peer: "raw.base.Peer", default_banned_rights: "raw.base.ChatBannedRights", version: int) -> None:
        self.peer = peer  # Peer
        self.default_banned_rights = default_banned_rights  # ChatBannedRights
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatDefaultBannedRights":
        # No flags

        peer = TLObject.read(b)

        default_banned_rights = TLObject.read(b)

        version = Int.read(b)

        return UpdateChatDefaultBannedRights(peer=peer, default_banned_rights=default_banned_rights, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.default_banned_rights.write())

        b.write(Int(self.version))

        return b.getvalue()
