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


class UpdateChannelUserTyping(TLObject):  # type: ignore
    """A user is typing in a supergroup, channel or message thread

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8C88C923``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer that is typing

        action (:obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`):
            Whether the user is typing, sending a media or doing something else

        top_msg_id (``int`` ``32-bit``, *optional*):
            Thread ID

    """

    __slots__: List[str] = ["channel_id", "from_id", "action", "top_msg_id"]

    ID = 0x8c88c923
    QUALNAME = "types.UpdateChannelUserTyping"

    def __init__(self, *, channel_id: int, from_id: "raw.base.Peer", action: "raw.base.SendMessageAction", top_msg_id: Optional[int] = None) -> None:
        self.channel_id = channel_id  # long
        self.from_id = from_id  # Peer
        self.action = action  # SendMessageAction
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelUserTyping":

        flags = Int.read(b)

        channel_id = Long.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        from_id = TLObject.read(b)

        action = TLObject.read(b)

        return UpdateChannelUserTyping(channel_id=channel_id, from_id=from_id, action=action, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))

        b.write(Long(self.channel_id))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        b.write(self.from_id.write())

        b.write(self.action.write())

        return b.getvalue()
