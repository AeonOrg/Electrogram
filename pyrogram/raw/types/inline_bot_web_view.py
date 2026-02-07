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


class InlineBotWebView(TLObject):  # type: ignore
    """Specifies an inline mode mini app button, shown on top of the inline query results list.

    Constructor of :obj:`~pyrogram.raw.base.InlineBotWebView`.

    Details:
        - Layer: ``224``
        - ID: ``B57295D5``

    Parameters:
        text (``str``):
            Text of the button

        url (``str``):
            Webapp URL

    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xb57295d5
    QUALNAME = "types.InlineBotWebView"

    def __init__(self, *, text: str, url: str) -> None:
        self.text = text  # string
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotWebView":
        # No flags

        text = String.read(b)

        url = String.read(b)

        return InlineBotWebView(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(String(self.url))

        return b.getvalue()
