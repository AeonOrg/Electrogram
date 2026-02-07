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


class ToggleGroupCallStartSubscription(TLObject):  # type: ignore
    """Subscribe or unsubscribe to a scheduled group call


    Details:
        - Layer: ``224``
        - ID: ``219C34E6``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Scheduled group call

        subscribed (``bool``):
            Enable or disable subscription

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "subscribed"]

    ID = 0x219c34e6
    QUALNAME = "functions.phone.ToggleGroupCallStartSubscription"

    def __init__(self, *, call: "raw.base.InputGroupCall", subscribed: bool) -> None:
        self.call = call  # InputGroupCall
        self.subscribed = subscribed  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallStartSubscription":
        # No flags

        call = TLObject.read(b)

        subscribed = Bool.read(b)

        return ToggleGroupCallStartSubscription(call=call, subscribed=subscribed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Bool(self.subscribed))

        return b.getvalue()
