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


class UpdatePeerSettings(TLObject):  # type: ignore
    """Settings of a certain peer have changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``6A7E7366``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer

        settings (:obj:`PeerSettings <pyrogram.raw.base.PeerSettings>`):
            Associated peer settings

    """

    __slots__: List[str] = ["peer", "settings"]

    ID = 0x6a7e7366
    QUALNAME = "types.UpdatePeerSettings"

    def __init__(self, *, peer: "raw.base.Peer", settings: "raw.base.PeerSettings") -> None:
        self.peer = peer  # Peer
        self.settings = settings  # PeerSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerSettings":
        # No flags

        peer = TLObject.read(b)

        settings = TLObject.read(b)

        return UpdatePeerSettings(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.settings.write())

        return b.getvalue()
