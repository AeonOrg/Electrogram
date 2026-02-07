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


class EditGroupCallTitle(TLObject):  # type: ignore
    """Edit the title of a group call or livestream


    Details:
        - Layer: ``224``
        - ID: ``1CA6AC0A``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

        title (``str``):
            New title

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "title"]

    ID = 0x1ca6ac0a
    QUALNAME = "functions.phone.EditGroupCallTitle"

    def __init__(self, *, call: "raw.base.InputGroupCall", title: str) -> None:
        self.call = call  # InputGroupCall
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditGroupCallTitle":
        # No flags

        call = TLObject.read(b)

        title = String.read(b)

        return EditGroupCallTitle(call=call, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(String(self.title))

        return b.getvalue()
