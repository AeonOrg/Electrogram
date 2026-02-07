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


class LeaveGroupCallPresentation(TLObject):  # type: ignore
    """Stop screen sharing in a group call


    Details:
        - Layer: ``224``
        - ID: ``1C50D144``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            The group call

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x1c50d144
    QUALNAME = "functions.phone.LeaveGroupCallPresentation"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call  # InputGroupCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveGroupCallPresentation":
        # No flags

        call = TLObject.read(b)

        return LeaveGroupCallPresentation(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        return b.getvalue()
