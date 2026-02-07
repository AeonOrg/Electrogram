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


class InlineBotSwitchPM(TLObject):  # type: ignore
    """The bot requested the user to message them in private

    Constructor of :obj:`~pyrogram.raw.base.InlineBotSwitchPM`.

    Details:
        - Layer: ``224``
        - ID: ``3C20629F``

    Parameters:
        text (``str``):
            Text for the button that switches the user to a private chat with the bot and sends the bot a start message with the parameter start_parameter (can be empty)

        start_param (``str``):
            The parameter for the /start parameter

    """

    __slots__: List[str] = ["text", "start_param"]

    ID = 0x3c20629f
    QUALNAME = "types.InlineBotSwitchPM"

    def __init__(self, *, text: str, start_param: str) -> None:
        self.text = text  # string
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotSwitchPM":
        # No flags

        text = String.read(b)

        start_param = String.read(b)

        return InlineBotSwitchPM(text=text, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(String(self.start_param))

        return b.getvalue()
