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


class GetPeerMaxIDs(TLObject):  # type: ignore
    """Get the IDs of the maximum read stories for a set of peers.


    Details:
        - Layer: ``224``
        - ID: ``78499170``

    Parameters:
        id (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peers

    Returns:
        List of :obj:`RecentStory <pyrogram.raw.base.RecentStory>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x78499170
    QUALNAME = "functions.stories.GetPeerMaxIDs"

    def __init__(self, *, id: List["raw.base.InputPeer"]) -> None:
        self.id = id  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerMaxIDs":
        # No flags

        id = TLObject.read(b)

        return GetPeerMaxIDs(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id))

        return b.getvalue()
