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


class WebViewResult(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.WebViewResult`.

    Details:
        - Layer: ``224``
        - ID: ``AADF159B``

    Parameters:
        result (:obj:`BotInlineResult <pyrogram.raw.base.BotInlineResult>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebViewResult
    """

    __slots__: List[str] = ["result", "users"]

    ID = 0xaadf159b
    QUALNAME = "types.messages.WebViewResult"

    def __init__(self, *, result: "raw.base.BotInlineResult", users: List["raw.base.User"]) -> None:
        self.result = result  # BotInlineResult
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewResult":
        # No flags

        result = TLObject.read(b)

        users = TLObject.read(b)

        return WebViewResult(result=result, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.result.write())

        b.write(Vector(self.users))

        return b.getvalue()
