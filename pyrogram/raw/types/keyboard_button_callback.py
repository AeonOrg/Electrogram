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


class KeyboardButtonCallback(TLObject):  # type: ignore
    """Callback button

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``E62BC960``

    Parameters:
        text (``str``):
            Button text

        data (``bytes``):
            Callback data

        requires_password (``bool``, *optional*):
            Whether the user should verify his identity by entering his 2FA SRP parameters to the messages.getBotCallbackAnswer method. NOTE: telegram and the bot WILL NOT have access to the plaintext password, thanks to SRP. This button is mainly used by the official @botfather bot, for verifying the user's identity before transferring ownership of a bot to another user.

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "data", "requires_password", "style"]

    ID = 0xe62bc960
    QUALNAME = "types.KeyboardButtonCallback"

    def __init__(self, *, text: str, data: bytes, requires_password: Optional[bool] = None, style: "raw.base.KeyboardButtonStyle" = None) -> None:
        self.text = text  # string
        self.data = data  # bytes
        self.requires_password = requires_password  # flags.0?true
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCallback":

        flags = Int.read(b)

        requires_password = True if flags & (1 << 0) else False
        style = TLObject.read(b) if flags & (1 << 10) else None

        text = String.read(b)

        data = Bytes.read(b)

        return KeyboardButtonCallback(text=text, data=data, requires_password=requires_password, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requires_password else 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        b.write(Bytes(self.data))

        return b.getvalue()
