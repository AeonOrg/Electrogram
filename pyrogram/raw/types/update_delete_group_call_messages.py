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


class UpdateDeleteGroupCallMessages(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``3E85E92C``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["call", "messages"]

    ID = 0x3e85e92c
    QUALNAME = "types.UpdateDeleteGroupCallMessages"

    def __init__(self, *, call: "raw.base.InputGroupCall", messages: List[int]) -> None:
        self.call = call  # InputGroupCall
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteGroupCallMessages":
        # No flags

        call = TLObject.read(b)

        messages = TLObject.read(b, Int)

        return UpdateDeleteGroupCallMessages(call=call, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Vector(self.messages, Int))

        return b.getvalue()
