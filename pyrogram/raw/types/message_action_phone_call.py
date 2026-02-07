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


class MessageActionPhoneCall(TLObject):  # type: ignore
    """A phone call

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``80E11A7F``

    Parameters:
        call_id (``int`` ``64-bit``):
            Call ID

        video (``bool``, *optional*):
            Is this a video call?

        reason (:obj:`PhoneCallDiscardReason <pyrogram.raw.base.PhoneCallDiscardReason>`, *optional*):
            If the call has ended, the reason why it ended

        duration (``int`` ``32-bit``, *optional*):
            Duration of the call in seconds

    """

    __slots__: List[str] = ["call_id", "video", "reason", "duration"]

    ID = 0x80e11a7f
    QUALNAME = "types.MessageActionPhoneCall"

    def __init__(self, *, call_id: int, video: Optional[bool] = None, reason: "raw.base.PhoneCallDiscardReason" = None, duration: Optional[int] = None) -> None:
        self.call_id = call_id  # long
        self.video = video  # flags.2?true
        self.reason = reason  # flags.0?PhoneCallDiscardReason
        self.duration = duration  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPhoneCall":

        flags = Int.read(b)

        video = True if flags & (1 << 2) else False
        call_id = Long.read(b)

        reason = TLObject.read(b) if flags & (1 << 0) else None

        duration = Int.read(b) if flags & (1 << 1) else None
        return MessageActionPhoneCall(call_id=call_id, video=video, reason=reason, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.video else 0
        flags |= (1 << 0) if self.reason is not None else 0
        flags |= (1 << 1) if self.duration is not None else 0
        b.write(Int(flags))

        b.write(Long(self.call_id))

        if self.reason is not None:
            b.write(self.reason.write())

        if self.duration is not None:
            b.write(Int(self.duration))

        return b.getvalue()
