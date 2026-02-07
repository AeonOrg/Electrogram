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


class DisablePeerConnectedBot(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``5E437ED9``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x5e437ed9
    QUALNAME = "functions.account.DisablePeerConnectedBot"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DisablePeerConnectedBot":
        # No flags

        peer = TLObject.read(b)

        return DisablePeerConnectedBot(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
