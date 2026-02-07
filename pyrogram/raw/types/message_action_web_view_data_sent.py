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


class MessageActionWebViewDataSent(TLObject):  # type: ignore
    """Data from an opened reply keyboard bot mini app was relayed to the bot that owns it (user side service message).

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B4C38CB5``

    Parameters:
        text (``str``):
            Text of the keyboardButtonSimpleWebView that was pressed to open the web app.

    """

    __slots__: List[str] = ["text"]

    ID = 0xb4c38cb5
    QUALNAME = "types.MessageActionWebViewDataSent"

    def __init__(self, *, text: str) -> None:
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionWebViewDataSent":
        # No flags

        text = String.read(b)

        return MessageActionWebViewDataSent(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        return b.getvalue()
