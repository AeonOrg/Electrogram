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


class CanSendStory(TLObject):  # type: ignore
    """Check whether we can post stories as the specified peer.


    Details:
        - Layer: ``224``
        - ID: ``30EB63F0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer from which we wish to post stories.

    Returns:
        :obj:`stories.CanSendStoryCount <pyrogram.raw.base.stories.CanSendStoryCount>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x30eb63f0
    QUALNAME = "functions.stories.CanSendStory"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CanSendStory":
        # No flags

        peer = TLObject.read(b)

        return CanSendStory(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
