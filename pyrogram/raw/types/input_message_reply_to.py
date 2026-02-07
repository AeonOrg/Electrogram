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


class InputMessageReplyTo(TLObject):  # type: ignore
    """Message to which the specified message replies to

    Constructor of :obj:`~pyrogram.raw.base.InputMessage`.

    Details:
        - Layer: ``224``
        - ID: ``BAD88395``

    Parameters:
        id (``int`` ``32-bit``):
            ID of the message that replies to the message we need

    """

    __slots__: List[str] = ["id"]

    ID = 0xbad88395
    QUALNAME = "types.InputMessageReplyTo"

    def __init__(self, *, id: int) -> None:
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageReplyTo":
        # No flags

        id = Int.read(b)

        return InputMessageReplyTo(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.id))

        return b.getvalue()
