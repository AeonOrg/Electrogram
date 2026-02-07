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


class SendGroupCallMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B1D11410``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "random_id", "message", "allow_paid_stars", "send_as"]

    ID = 0xb1d11410
    QUALNAME = "functions.phone.SendGroupCallMessage"

    def __init__(self, *, call: "raw.base.InputGroupCall", random_id: int, message: "raw.base.TextWithEntities", allow_paid_stars: Optional[int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.call = call  # InputGroupCall
        self.random_id = random_id  # long
        self.message = message  # TextWithEntities
        self.allow_paid_stars = allow_paid_stars  # flags.0?long
        self.send_as = send_as  # flags.1?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendGroupCallMessage":

        flags = Int.read(b)

        call = TLObject.read(b)

        random_id = Long.read(b)

        message = TLObject.read(b)

        allow_paid_stars = Long.read(b) if flags & (1 << 0) else None
        send_as = TLObject.read(b) if flags & (1 << 1) else None

        return SendGroupCallMessage(call=call, random_id=random_id, message=message, allow_paid_stars=allow_paid_stars, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_paid_stars is not None else 0
        flags |= (1 << 1) if self.send_as is not None else 0
        b.write(Int(flags))

        b.write(self.call.write())

        b.write(Long(self.random_id))

        b.write(self.message.write())

        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))

        if self.send_as is not None:
            b.write(self.send_as.write())

        return b.getvalue()
