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


class UpdateReadChannelDiscussionOutbox(TLObject):  # type: ignore
    """Outgoing comments in a discussion thread were marked as read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``695C9E7C``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Supergroup ID

        top_msg_id (``int`` ``32-bit``):
            ID of the group message that started the thread

        read_max_id (``int`` ``32-bit``):
            Message ID of latest read outgoing message for this thread

    """

    __slots__: List[str] = ["channel_id", "top_msg_id", "read_max_id"]

    ID = 0x695c9e7c
    QUALNAME = "types.UpdateReadChannelDiscussionOutbox"

    def __init__(self, *, channel_id: int, top_msg_id: int, read_max_id: int) -> None:
        self.channel_id = channel_id  # long
        self.top_msg_id = top_msg_id  # int
        self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelDiscussionOutbox":
        # No flags

        channel_id = Long.read(b)

        top_msg_id = Int.read(b)

        read_max_id = Int.read(b)

        return UpdateReadChannelDiscussionOutbox(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Int(self.top_msg_id))

        b.write(Int(self.read_max_id))

        return b.getvalue()
