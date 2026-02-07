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


class BotMenuButton(TLObject):  # type: ignore
    """Bot menu button that opens a web app when clicked.

    Constructor of :obj:`~pyrogram.raw.base.BotMenuButton`.

    Details:
        - Layer: ``224``
        - ID: ``C7B57CE6``

    Parameters:
        text (``str``):
            Title to be displayed on the menu button instead of 'Menu'

        url (``str``):
            URL of a web app to open when the user clicks on the button

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xc7b57ce6
    QUALNAME = "types.BotMenuButton"

    def __init__(self, *, text: str, url: str) -> None:
        self.text = text  # string
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotMenuButton":
        # No flags

        text = String.read(b)

        url = String.read(b)

        return BotMenuButton(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(String(self.url))

        return b.getvalue()
