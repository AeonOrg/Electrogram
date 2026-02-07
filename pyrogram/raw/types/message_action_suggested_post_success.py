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


class MessageActionSuggestedPostSuccess(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``95DDCF69``

    Parameters:
        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

    """

    __slots__: List[str] = ["price"]

    ID = 0x95ddcf69
    QUALNAME = "types.MessageActionSuggestedPostSuccess"

    def __init__(self, *, price: "raw.base.StarsAmount") -> None:
        self.price = price  # StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestedPostSuccess":
        # No flags

        price = TLObject.read(b)

        return MessageActionSuggestedPostSuccess(price=price)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.price.write())

        return b.getvalue()
