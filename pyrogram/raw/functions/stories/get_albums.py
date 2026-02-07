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


class GetAlbums(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``25B3EAC7``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`stories.Albums <pyrogram.raw.base.stories.Albums>`
    """

    __slots__: List[str] = ["peer", "hash"]

    ID = 0x25b3eac7
    QUALNAME = "functions.stories.GetAlbums"

    def __init__(self, *, peer: "raw.base.InputPeer", hash: int) -> None:
        self.peer = peer  # InputPeer
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAlbums":
        # No flags

        peer = TLObject.read(b)

        hash = Long.read(b)

        return GetAlbums(peer=peer, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Long(self.hash))

        return b.getvalue()
