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


class GetBotApp(TLObject):  # type: ignore
    """Obtain information about a direct link Mini App


    Details:
        - Layer: ``224``
        - ID: ``34FDC5C3``

    Parameters:
        app (:obj:`InputBotApp <pyrogram.raw.base.InputBotApp>`):
            Bot app information obtained from a Direct Mini App deep link ».

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.BotApp <pyrogram.raw.base.messages.BotApp>`
    """

    __slots__: List[str] = ["app", "hash"]

    ID = 0x34fdc5c3
    QUALNAME = "functions.messages.GetBotApp"

    def __init__(self, *, app: "raw.base.InputBotApp", hash: int) -> None:
        self.app = app  # InputBotApp
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotApp":
        # No flags

        app = TLObject.read(b)

        hash = Long.read(b)

        return GetBotApp(app=app, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.app.write())

        b.write(Long(self.hash))

        return b.getvalue()
