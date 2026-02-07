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


class SendWebViewResultMessage(TLObject):  # type: ignore
    """Terminate webview interaction started with messages.requestWebView, sending the specified message to the chat on behalf of the user.


    Details:
        - Layer: ``224``
        - ID: ``A4314F5``

    Parameters:
        bot_query_id (``str``):
            Webview interaction ID obtained from messages.requestWebView

        result (:obj:`InputBotInlineResult <pyrogram.raw.base.InputBotInlineResult>`):
            Message to send

    Returns:
        :obj:`WebViewMessageSent <pyrogram.raw.base.WebViewMessageSent>`
    """

    __slots__: List[str] = ["bot_query_id", "result"]

    ID = 0xa4314f5
    QUALNAME = "functions.messages.SendWebViewResultMessage"

    def __init__(self, *, bot_query_id: str, result: "raw.base.InputBotInlineResult") -> None:
        self.bot_query_id = bot_query_id  # string
        self.result = result  # InputBotInlineResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendWebViewResultMessage":
        # No flags

        bot_query_id = String.read(b)

        result = TLObject.read(b)

        return SendWebViewResultMessage(bot_query_id=bot_query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.bot_query_id))

        b.write(self.result.write())

        return b.getvalue()
