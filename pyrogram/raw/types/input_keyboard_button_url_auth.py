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


class InputKeyboardButtonUrlAuth(TLObject):  # type: ignore
    """Button to request a user to authorize via URL using Seamless Telegram Login.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``68013E72``

    Parameters:
        text (``str``):
            Button text

        url (``str``):
            An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

        request_write_access (``bool``, *optional*):
            Set this flag to request the permission for your bot to send messages to the user.

        fwd_text (``str``, *optional*):
            New text of the button in forwarded messages.

    """

    __slots__: List[str] = ["text", "url", "bot", "style", "request_write_access", "fwd_text"]

    ID = 0x68013e72
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot: "raw.base.InputUser", style: "raw.base.KeyboardButtonStyle" = None, request_write_access: Optional[bool] = None, fwd_text: Optional[str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.bot = bot  # InputUser
        self.style = style  # flags.10?KeyboardButtonStyle
        self.request_write_access = request_write_access  # flags.0?true
        self.fwd_text = fwd_text  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        request_write_access = True if flags & (1 << 0) else False
        text = String.read(b)

        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)

        bot = TLObject.read(b)

        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, style=style, request_write_access=request_write_access, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        if self.fwd_text is not None:
            b.write(String(self.fwd_text))

        b.write(String(self.url))

        b.write(self.bot.write())

        return b.getvalue()
