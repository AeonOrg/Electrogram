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


class InputKeyboardButtonUserProfile(TLObject):  # type: ignore
    """Button that links directly to a user profile

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``7D5E07C7``

    Parameters:
        text (``str``):
            Button text

        input_user (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "input_user", "style"]

    ID = 0x7d5e07c7
    QUALNAME = "types.InputKeyboardButtonUserProfile"

    def __init__(self, *, text: str, input_user: "raw.base.InputUser", style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text  # string
        self.input_user = input_user  # InputUser
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUserProfile":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        text = String.read(b)

        input_user = TLObject.read(b)

        return InputKeyboardButtonUserProfile(text=text, input_user=input_user, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        b.write(self.input_user.write())

        return b.getvalue()
