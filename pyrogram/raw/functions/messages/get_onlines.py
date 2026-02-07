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


class GetOnlines(TLObject):  # type: ignore
    """Get count of online users in a chat


    Details:
        - Layer: ``224``
        - ID: ``6E2BE050``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat

    Returns:
        :obj:`ChatOnlines <pyrogram.raw.base.ChatOnlines>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x6e2be050
    QUALNAME = "functions.messages.GetOnlines"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetOnlines":
        # No flags

        peer = TLObject.read(b)

        return GetOnlines(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
