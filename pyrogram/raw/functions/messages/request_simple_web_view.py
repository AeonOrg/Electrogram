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


class RequestSimpleWebView(TLObject):  # type: ignore
    """Open a bot mini app.


    Details:
        - Layer: ``224``
        - ID: ``413A3E73``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Bot that owns the mini app

        platform (``str``):
            Short name of the application; 0-64 English letters, digits, and underscores

        from_switch_webview (``bool``, *optional*):
            Whether the webapp was opened by clicking on the switch_webview button shown on top of the inline results list returned by messages.getInlineBotResults.

        from_side_menu (``bool``, *optional*):
            Set this flag if opening the Mini App from the installed side menu entry » or from a Mini App link ».

        compact (``bool``, *optional*):
            N/A

        fullscreen (``bool``, *optional*):
            N/A

        url (``str``, *optional*):
            Web app URL, if opening from a keyboard button or inline result

        start_param (``str``, *optional*):
            Start parameter, if opening from a Mini App link ».

        theme_params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`, *optional*):
            Theme parameters »

    Returns:
        :obj:`WebViewResult <pyrogram.raw.base.WebViewResult>`
    """

    __slots__: List[str] = ["bot", "platform", "from_switch_webview", "from_side_menu", "compact", "fullscreen", "url", "start_param", "theme_params"]

    ID = 0x413a3e73
    QUALNAME = "functions.messages.RequestSimpleWebView"

    def __init__(self, *, bot: "raw.base.InputUser", platform: str, from_switch_webview: Optional[bool] = None, from_side_menu: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: "raw.base.DataJSON" = None) -> None:
        self.bot = bot  # InputUser
        self.platform = platform  # string
        self.from_switch_webview = from_switch_webview  # flags.1?true
        self.from_side_menu = from_side_menu  # flags.2?true
        self.compact = compact  # flags.7?true
        self.fullscreen = fullscreen  # flags.8?true
        self.url = url  # flags.3?string
        self.start_param = start_param  # flags.4?string
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestSimpleWebView":

        flags = Int.read(b)

        from_switch_webview = True if flags & (1 << 1) else False
        from_side_menu = True if flags & (1 << 2) else False
        compact = True if flags & (1 << 7) else False
        fullscreen = True if flags & (1 << 8) else False
        bot = TLObject.read(b)

        url = String.read(b) if flags & (1 << 3) else None
        start_param = String.read(b) if flags & (1 << 4) else None
        theme_params = TLObject.read(b) if flags & (1 << 0) else None

        platform = String.read(b)

        return RequestSimpleWebView(bot=bot, platform=platform, from_switch_webview=from_switch_webview, from_side_menu=from_side_menu, compact=compact, fullscreen=fullscreen, url=url, start_param=start_param, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.from_switch_webview else 0
        flags |= (1 << 2) if self.from_side_menu else 0
        flags |= (1 << 7) if self.compact else 0
        flags |= (1 << 8) if self.fullscreen else 0
        flags |= (1 << 3) if self.url is not None else 0
        flags |= (1 << 4) if self.start_param is not None else 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))

        b.write(self.bot.write())

        if self.url is not None:
            b.write(String(self.url))

        if self.start_param is not None:
            b.write(String(self.start_param))

        if self.theme_params is not None:
            b.write(self.theme_params.write())

        b.write(String(self.platform))

        return b.getvalue()
