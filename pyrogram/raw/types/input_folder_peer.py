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


class InputFolderPeer(TLObject):  # type: ignore
    """Peer in a folder

    Constructor of :obj:`~pyrogram.raw.base.InputFolderPeer`.

    Details:
        - Layer: ``224``
        - ID: ``FBD2C296``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer

        folder_id (``int`` ``32-bit``):
            Peer folder ID, for more info click here

    """

    __slots__: List[str] = ["peer", "folder_id"]

    ID = 0xfbd2c296
    QUALNAME = "types.InputFolderPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", folder_id: int) -> None:
        self.peer = peer  # InputPeer
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFolderPeer":
        # No flags

        peer = TLObject.read(b)

        folder_id = Int.read(b)

        return InputFolderPeer(peer=peer, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.folder_id))

        return b.getvalue()
