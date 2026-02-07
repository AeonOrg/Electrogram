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


class GetGroupCallJoinAs(TLObject):  # type: ignore
    """Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.


    Details:
        - Layer: ``224``
        - ID: ``EF7C213A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The dialog whose group call or livestream we're trying to join

    Returns:
        :obj:`phone.JoinAsPeers <pyrogram.raw.base.phone.JoinAsPeers>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0xef7c213a
    QUALNAME = "functions.phone.GetGroupCallJoinAs"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallJoinAs":
        # No flags

        peer = TLObject.read(b)

        return GetGroupCallJoinAs(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
