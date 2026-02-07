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


class UpdateChannelReadMessagesContents(TLObject):  # type: ignore
    """The specified channel/supergroup messages were read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``25F324F7``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel/supergroup ID

        messages (List of ``int`` ``32-bit``):
            IDs of messages that were read

        top_msg_id (``int`` ``32-bit``, *optional*):
            Forum topic ID.

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["channel_id", "messages", "top_msg_id", "saved_peer_id"]

    ID = 0x25f324f7
    QUALNAME = "types.UpdateChannelReadMessagesContents"

    def __init__(self, *, channel_id: int, messages: List[int], top_msg_id: Optional[int] = None, saved_peer_id: "raw.base.Peer" = None) -> None:
        self.channel_id = channel_id  # long
        self.messages = messages  # Vector<int>
        self.top_msg_id = top_msg_id  # flags.0?int
        self.saved_peer_id = saved_peer_id  # flags.1?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelReadMessagesContents":

        flags = Int.read(b)

        channel_id = Long.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        saved_peer_id = TLObject.read(b) if flags & (1 << 1) else None

        messages = TLObject.read(b, Int)

        return UpdateChannelReadMessagesContents(channel_id=channel_id, messages=messages, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.saved_peer_id is not None else 0
        b.write(Int(flags))

        b.write(Long(self.channel_id))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        b.write(Vector(self.messages, Int))

        return b.getvalue()
