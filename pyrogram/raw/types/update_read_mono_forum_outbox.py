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


class UpdateReadMonoForumOutbox(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``A4A79376``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        read_max_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id", "saved_peer_id", "read_max_id"]

    ID = 0xa4a79376
    QUALNAME = "types.UpdateReadMonoForumOutbox"

    def __init__(self, *, channel_id: int, saved_peer_id: "raw.base.Peer", read_max_id: int) -> None:
        self.channel_id = channel_id  # long
        self.saved_peer_id = saved_peer_id  # Peer
        self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadMonoForumOutbox":
        # No flags

        channel_id = Long.read(b)

        saved_peer_id = TLObject.read(b)

        read_max_id = Int.read(b)

        return UpdateReadMonoForumOutbox(channel_id=channel_id, saved_peer_id=saved_peer_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(self.saved_peer_id.write())

        b.write(Int(self.read_max_id))

        return b.getvalue()
