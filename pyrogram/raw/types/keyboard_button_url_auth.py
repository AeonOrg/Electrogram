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


class KeyboardButtonUrlAuth(TLObject):  # type: ignore
    """Button to request a user to authorize via URL using Seamless Telegram Login. When the user clicks on such a button, messages.requestUrlAuth should be called, providing the button_id and the ID of the container message. The returned urlAuthResultRequest object will contain more details about the authorization request (request_write_access if the bot would like to send messages to the user along with the username of the bot which will be used for user authorization). Finally, the user can choose to call messages.acceptUrlAuth to get a urlAuthResultAccepted with the URL to open instead of the url of this constructor, or a urlAuthResultDefault, in which case the url of this constructor must be opened, instead. If the user refuses the authorization request but still wants to open the link, the url of this constructor must be used.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``F51006F9``

    Parameters:
        text (``str``):
            Button label

        url (``str``):
            An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: Services must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.

        button_id (``int`` ``32-bit``):
            ID of the button to pass to messages.requestUrlAuth

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

        fwd_text (``str``, *optional*):
            New text of the button in forwarded messages.

    """

    __slots__: List[str] = ["text", "url", "button_id", "style", "fwd_text"]

    ID = 0xf51006f9
    QUALNAME = "types.KeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, button_id: int, style: "raw.base.KeyboardButtonStyle" = None, fwd_text: Optional[str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.button_id = button_id  # int
        self.style = style  # flags.10?KeyboardButtonStyle
        self.fwd_text = fwd_text  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonUrlAuth":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        text = String.read(b)

        fwd_text = String.read(b) if flags & (1 << 0) else None
        url = String.read(b)

        button_id = Int.read(b)

        return KeyboardButtonUrlAuth(text=text, url=url, button_id=button_id, style=style, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 0) if self.fwd_text is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        b.write(String(self.text))

        if self.fwd_text is not None:
            b.write(String(self.fwd_text))

        b.write(String(self.url))

        b.write(Int(self.button_id))

        return b.getvalue()
