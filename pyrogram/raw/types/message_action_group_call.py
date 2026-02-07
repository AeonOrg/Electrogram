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


class MessageActionGroupCall(TLObject):  # type: ignore
    """The group call has ended

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``7A0D7F42``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

        duration (``int`` ``32-bit``, *optional*):
            Group call duration

    """

    __slots__: List[str] = ["call", "duration"]

    ID = 0x7a0d7f42
    QUALNAME = "types.MessageActionGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", duration: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.duration = duration  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCall":

        flags = Int.read(b)

        call = TLObject.read(b)

        duration = Int.read(b) if flags & (1 << 0) else None
        return MessageActionGroupCall(call=call, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration is not None else 0
        b.write(Int(flags))

        b.write(self.call.write())

        if self.duration is not None:
            b.write(Int(self.duration))

        return b.getvalue()
