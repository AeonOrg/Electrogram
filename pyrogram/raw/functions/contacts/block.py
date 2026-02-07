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


class Block(TLObject):  # type: ignore
    """Adds a peer to a blocklist, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``2E2E8734``

    Parameters:
        id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer

        my_stories_from (``bool``, *optional*):
            Whether the peer should be added to the story blocklist; if not set, the peer will be added to the main blocklist, see here » for more info.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "my_stories_from"]

    ID = 0x2e2e8734
    QUALNAME = "functions.contacts.Block"

    def __init__(self, *, id: "raw.base.InputPeer", my_stories_from: Optional[bool] = None) -> None:
        self.id = id  # InputPeer
        self.my_stories_from = my_stories_from  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Block":

        flags = Int.read(b)

        my_stories_from = True if flags & (1 << 0) else False
        id = TLObject.read(b)

        return Block(id=id, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.my_stories_from else 0
        b.write(Int(flags))

        b.write(self.id.write())

        return b.getvalue()
