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


class ExportStoryLink(TLObject):  # type: ignore
    """Generate a story deep link for a specific story


    Details:
        - Layer: ``224``
        - ID: ``7B8DEF20``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the story was posted

        id (``int`` ``32-bit``):
            Story ID

    Returns:
        :obj:`ExportedStoryLink <pyrogram.raw.base.ExportedStoryLink>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x7b8def20
    QUALNAME = "functions.stories.ExportStoryLink"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportStoryLink":
        # No flags

        peer = TLObject.read(b)

        id = Int.read(b)

        return ExportStoryLink(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.id))

        return b.getvalue()
