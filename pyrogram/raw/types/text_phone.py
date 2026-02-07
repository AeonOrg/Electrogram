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


class TextPhone(TLObject):  # type: ignore
    """Rich text linked to a phone number

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``224``
        - ID: ``1CCB966A``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Text

        phone (``str``):
            Phone number

    """

    __slots__: List[str] = ["text", "phone"]

    ID = 0x1ccb966a
    QUALNAME = "types.TextPhone"

    def __init__(self, *, text: "raw.base.RichText", phone: str) -> None:
        self.text = text  # RichText
        self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextPhone":
        # No flags

        text = TLObject.read(b)

        phone = String.read(b)

        return TextPhone(text=text, phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        b.write(String(self.phone))

        return b.getvalue()
