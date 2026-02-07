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


class InputMediaStory(TLObject):  # type: ignore
    """Forwarded story

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``89FDD778``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the story was posted

        id (``int`` ``32-bit``):
            Story ID

    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x89fdd778
    QUALNAME = "types.InputMediaStory"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaStory":
        # No flags

        peer = TLObject.read(b)

        id = Int.read(b)

        return InputMediaStory(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.id))

        return b.getvalue()
