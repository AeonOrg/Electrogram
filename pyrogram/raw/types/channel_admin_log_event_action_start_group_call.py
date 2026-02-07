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


class ChannelAdminLogEventActionStartGroupCall(TLObject):  # type: ignore
    """A group call was started

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``23209745``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

    """

    __slots__: List[str] = ["call"]

    ID = 0x23209745
    QUALNAME = "types.ChannelAdminLogEventActionStartGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call  # InputGroupCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionStartGroupCall":
        # No flags

        call = TLObject.read(b)

        return ChannelAdminLogEventActionStartGroupCall(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        return b.getvalue()
