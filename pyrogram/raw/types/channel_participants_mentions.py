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


class ChannelParticipantsMentions(TLObject):  # type: ignore
    """This filter is used when looking for supergroup members to mention.
This filter will automatically remove anonymous admins, and return even non-participant users that replied to a specific thread through the comment section of a channel.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipantsFilter`.

    Details:
        - Layer: ``224``
        - ID: ``E04B5CEB``

    Parameters:
        q (``str``, *optional*):
            Filter by user name or username

        top_msg_id (``int`` ``32-bit``, *optional*):
            Look only for users that posted in this thread

    """

    __slots__: List[str] = ["q", "top_msg_id"]

    ID = 0xe04b5ceb
    QUALNAME = "types.ChannelParticipantsMentions"

    def __init__(self, *, q: Optional[str] = None, top_msg_id: Optional[int] = None) -> None:
        self.q = q  # flags.0?string
        self.top_msg_id = top_msg_id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantsMentions":

        flags = Int.read(b)

        q = String.read(b) if flags & (1 << 0) else None
        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        return ChannelParticipantsMentions(q=q, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.q is not None else 0
        flags |= (1 << 1) if self.top_msg_id is not None else 0
        b.write(Int(flags))

        if self.q is not None:
            b.write(String(self.q))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        return b.getvalue()
