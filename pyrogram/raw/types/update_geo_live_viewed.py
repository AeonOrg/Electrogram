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


class UpdateGeoLiveViewed(TLObject):  # type: ignore
    """Live geoposition message was viewed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``871FB939``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The user that viewed the live geoposition

        msg_id (``int`` ``32-bit``):
            Message ID of geoposition message

    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x871fb939
    QUALNAME = "types.UpdateGeoLiveViewed"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGeoLiveViewed":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        return UpdateGeoLiveViewed(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        return b.getvalue()
