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


class InputBotInlineResultGame(TLObject):  # type: ignore
    """Game

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``224``
        - ID: ``4FA417F2``

    Parameters:
        id (``str``):
            Result ID

        short_name (``str``):
            Game short name

        send_message (:obj:`InputBotInlineMessage <pyrogram.raw.base.InputBotInlineMessage>`):
            Message to send when the result is selected

    """

    __slots__: List[str] = ["id", "short_name", "send_message"]

    ID = 0x4fa417f2
    QUALNAME = "types.InputBotInlineResultGame"

    def __init__(self, *, id: str, short_name: str, send_message: "raw.base.InputBotInlineMessage") -> None:
        self.id = id  # string
        self.short_name = short_name  # string
        self.send_message = send_message  # InputBotInlineMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultGame":
        # No flags

        id = String.read(b)

        short_name = String.read(b)

        send_message = TLObject.read(b)

        return InputBotInlineResultGame(id=id, short_name=short_name, send_message=send_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        b.write(String(self.short_name))

        b.write(self.send_message.write())

        return b.getvalue()
