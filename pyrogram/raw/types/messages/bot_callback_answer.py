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


class BotCallbackAnswer(TLObject):  # type: ignore
    """Callback answer sent by the bot in response to a button press

    Constructor of :obj:`~pyrogram.raw.base.messages.BotCallbackAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``36585EA4``

    Parameters:
        cache_time (``int`` ``32-bit``):
            For how long should this answer be cached

        alert (``bool``, *optional*):
            Whether an alert should be shown to the user instead of a toast notification

        has_url (``bool``, *optional*):
            Whether an URL is present

        native_ui (``bool``, *optional*):
            Whether to show games in WebView or in native UI.

        message (``str``, *optional*):
            Alert to show

        url (``str``, *optional*):
            URL to open

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetBotCallbackAnswer
    """

    __slots__: List[str] = ["cache_time", "alert", "has_url", "native_ui", "message", "url"]

    ID = 0x36585ea4
    QUALNAME = "types.messages.BotCallbackAnswer"

    def __init__(self, *, cache_time: int, alert: Optional[bool] = None, has_url: Optional[bool] = None, native_ui: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None) -> None:
        self.cache_time = cache_time  # int
        self.alert = alert  # flags.1?true
        self.has_url = has_url  # flags.3?true
        self.native_ui = native_ui  # flags.4?true
        self.message = message  # flags.0?string
        self.url = url  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCallbackAnswer":

        flags = Int.read(b)

        alert = True if flags & (1 << 1) else False
        has_url = True if flags & (1 << 3) else False
        native_ui = True if flags & (1 << 4) else False
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)

        return BotCallbackAnswer(cache_time=cache_time, alert=alert, has_url=has_url, native_ui=native_ui, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert else 0
        flags |= (1 << 3) if self.has_url else 0
        flags |= (1 << 4) if self.native_ui else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))

        if self.message is not None:
            b.write(String(self.message))

        if self.url is not None:
            b.write(String(self.url))

        b.write(Int(self.cache_time))

        return b.getvalue()
