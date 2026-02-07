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


class MessageActionGroupCallScheduled(TLObject):  # type: ignore
    """A group call was scheduled

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B3A07661``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            The group call

        schedule_date (``int`` ``32-bit``):
            When is this group call scheduled to start

    """

    __slots__: List[str] = ["call", "schedule_date"]

    ID = 0xb3a07661
    QUALNAME = "types.MessageActionGroupCallScheduled"

    def __init__(self, *, call: "raw.base.InputGroupCall", schedule_date: int) -> None:
        self.call = call  # InputGroupCall
        self.schedule_date = schedule_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCallScheduled":
        # No flags

        call = TLObject.read(b)

        schedule_date = Int.read(b)

        return MessageActionGroupCallScheduled(call=call, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Int(self.schedule_date))

        return b.getvalue()
