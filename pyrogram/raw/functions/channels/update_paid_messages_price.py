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


class UpdatePaidMessagesPrice(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4B12327B``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``):
            N/A

        broadcast_messages_allowed (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "send_paid_messages_stars", "broadcast_messages_allowed"]

    ID = 0x4b12327b
    QUALNAME = "functions.channels.UpdatePaidMessagesPrice"

    def __init__(self, *, channel: "raw.base.InputChannel", send_paid_messages_stars: int, broadcast_messages_allowed: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.send_paid_messages_stars = send_paid_messages_stars  # long
        self.broadcast_messages_allowed = broadcast_messages_allowed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePaidMessagesPrice":

        flags = Int.read(b)

        broadcast_messages_allowed = True if flags & (1 << 0) else False
        channel = TLObject.read(b)

        send_paid_messages_stars = Long.read(b)

        return UpdatePaidMessagesPrice(channel=channel, send_paid_messages_stars=send_paid_messages_stars, broadcast_messages_allowed=broadcast_messages_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast_messages_allowed else 0
        b.write(Int(flags))

        b.write(self.channel.write())

        b.write(Long(self.send_paid_messages_stars))

        return b.getvalue()
