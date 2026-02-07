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


class EditPeerFolders(TLObject):  # type: ignore
    """Edit peers in peer folder


    Details:
        - Layer: ``224``
        - ID: ``6847D0AB``

    Parameters:
        folder_peers (List of :obj:`InputFolderPeer <pyrogram.raw.base.InputFolderPeer>`):
            New peer list

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["folder_peers"]

    ID = 0x6847d0ab
    QUALNAME = "functions.folders.EditPeerFolders"

    def __init__(self, *, folder_peers: List["raw.base.InputFolderPeer"]) -> None:
        self.folder_peers = folder_peers  # Vector<InputFolderPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditPeerFolders":
        # No flags

        folder_peers = TLObject.read(b)

        return EditPeerFolders(folder_peers=folder_peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.folder_peers))

        return b.getvalue()
