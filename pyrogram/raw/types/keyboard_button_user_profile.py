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


class KeyboardButtonUserProfile(TLObject):  # type: ignore
    """Button that links directly to a user profile

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``C0FD5D09``

    Parameters:
        text (``str``):
            Button text

        user_id (``int`` ``64-bit``):
            User ID

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "user_id", "style"]

    ID = 0xc0fd5d09
    QUALNAME = "types.KeyboardButtonUserProfile"

    def __init__(self, *, text: str, user_id: int, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text  # string
        self.user_id = user_id  # long
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonUserProfile":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        text = String.read(b)

        user_id = Long.read(b)

        return KeyboardButtonUserProfile(text=text, user_id=user_id, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        b.write(Long(self.user_id))

        return b.getvalue()
