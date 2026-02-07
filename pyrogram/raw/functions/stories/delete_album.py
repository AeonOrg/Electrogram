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


class DeleteAlbum(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8D3456D0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        album_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "album_id"]

    ID = 0x8d3456d0
    QUALNAME = "functions.stories.DeleteAlbum"

    def __init__(self, *, peer: "raw.base.InputPeer", album_id: int) -> None:
        self.peer = peer  # InputPeer
        self.album_id = album_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteAlbum":
        # No flags

        peer = TLObject.read(b)

        album_id = Int.read(b)

        return DeleteAlbum(peer=peer, album_id=album_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.album_id))

        return b.getvalue()
