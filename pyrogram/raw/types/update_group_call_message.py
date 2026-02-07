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


class UpdateGroupCallMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D8326F0D``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        message (:obj:`GroupCallMessage <pyrogram.raw.base.GroupCallMessage>`):
            N/A

    """

    __slots__: List[str] = ["call", "message"]

    ID = 0xd8326f0d
    QUALNAME = "types.UpdateGroupCallMessage"

    def __init__(self, *, call: "raw.base.InputGroupCall", message: "raw.base.GroupCallMessage") -> None:
        self.call = call  # InputGroupCall
        self.message = message  # GroupCallMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallMessage":
        # No flags

        call = TLObject.read(b)

        message = TLObject.read(b)

        return UpdateGroupCallMessage(call=call, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(self.message.write())

        return b.getvalue()
