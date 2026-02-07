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


class MessageActionSetChatTheme(TLObject):  # type: ignore
    """The chat theme was changed

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B91BBD3A``

    Parameters:
        theme (:obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`):
            N/A

    """

    __slots__: List[str] = ["theme"]

    ID = 0xb91bbd3a
    QUALNAME = "types.MessageActionSetChatTheme"

    def __init__(self, *, theme: "raw.base.ChatTheme") -> None:
        self.theme = theme  # ChatTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatTheme":
        # No flags

        theme = TLObject.read(b)

        return MessageActionSetChatTheme(theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.theme.write())

        return b.getvalue()
