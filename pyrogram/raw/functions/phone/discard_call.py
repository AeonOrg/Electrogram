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


class DiscardCall(TLObject):  # type: ignore
    """Refuse or end running call


    Details:
        - Layer: ``224``
        - ID: ``B2CBC1C0``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            The phone call

        duration (``int`` ``32-bit``):
            Call duration

        reason (:obj:`PhoneCallDiscardReason <pyrogram.raw.base.PhoneCallDiscardReason>`):
            Why was the call discarded

        connection_id (``int`` ``64-bit``):
            Preferred libtgvoip relay ID

        video (``bool``, *optional*):
            Whether this is a video call

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "duration", "reason", "connection_id", "video"]

    ID = 0xb2cbc1c0
    QUALNAME = "functions.phone.DiscardCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", duration: int, reason: "raw.base.PhoneCallDiscardReason", connection_id: int, video: Optional[bool] = None) -> None:
        self.peer = peer  # InputPhoneCall
        self.duration = duration  # int
        self.reason = reason  # PhoneCallDiscardReason
        self.connection_id = connection_id  # long
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscardCall":

        flags = Int.read(b)

        video = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        duration = Int.read(b)

        reason = TLObject.read(b)

        connection_id = Long.read(b)

        return DiscardCall(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.duration))

        b.write(self.reason.write())

        b.write(Long(self.connection_id))

        return b.getvalue()
