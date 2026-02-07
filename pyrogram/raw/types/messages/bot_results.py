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


class BotResults(TLObject):  # type: ignore
    """Result of a query to an inline bot

    Constructor of :obj:`~pyrogram.raw.base.messages.BotResults`.

    Details:
        - Layer: ``224``
        - ID: ``E021F2F6``

    Parameters:
        query_id (``int`` ``64-bit``):
            Query ID

        results (List of :obj:`BotInlineResult <pyrogram.raw.base.BotInlineResult>`):
            The results

        cache_time (``int`` ``32-bit``):
            Caching validity of the results

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in the results

        gallery (``bool``, *optional*):
            Whether the result is a picture gallery

        next_offset (``str``, *optional*):
            The next offset to use when navigating through results

        switch_pm (:obj:`InlineBotSwitchPM <pyrogram.raw.base.InlineBotSwitchPM>`, *optional*):
            Shown as a button on top of the remaining inline result list; if clicked, redirects the user to a private chat with the bot with the specified start parameter.

        switch_webview (:obj:`InlineBotWebView <pyrogram.raw.base.InlineBotWebView>`, *optional*):
            Shown as a button on top of the remaining inline result list; if clicked, opens the specified inline mode mini app.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetInlineBotResults
    """

    __slots__: List[str] = ["query_id", "results", "cache_time", "users", "gallery", "next_offset", "switch_pm", "switch_webview"]

    ID = 0xe021f2f6
    QUALNAME = "types.messages.BotResults"

    def __init__(self, *, query_id: int, results: List["raw.base.BotInlineResult"], cache_time: int, users: List["raw.base.User"], gallery: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: "raw.base.InlineBotSwitchPM" = None, switch_webview: "raw.base.InlineBotWebView" = None) -> None:
        self.query_id = query_id  # long
        self.results = results  # Vector<BotInlineResult>
        self.cache_time = cache_time  # int
        self.users = users  # Vector<User>
        self.gallery = gallery  # flags.0?true
        self.next_offset = next_offset  # flags.1?string
        self.switch_pm = switch_pm  # flags.2?InlineBotSwitchPM
        self.switch_webview = switch_webview  # flags.3?InlineBotWebView

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotResults":

        flags = Int.read(b)

        gallery = True if flags & (1 << 0) else False
        query_id = Long.read(b)

        next_offset = String.read(b) if flags & (1 << 1) else None
        switch_pm = TLObject.read(b) if flags & (1 << 2) else None

        switch_webview = TLObject.read(b) if flags & (1 << 3) else None

        results = TLObject.read(b)

        cache_time = Int.read(b)

        users = TLObject.read(b)

        return BotResults(query_id=query_id, results=results, cache_time=cache_time, users=users, gallery=gallery, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.gallery else 0
        flags |= (1 << 1) if self.next_offset is not None else 0
        flags |= (1 << 2) if self.switch_pm is not None else 0
        flags |= (1 << 3) if self.switch_webview is not None else 0
        b.write(Int(flags))

        b.write(Long(self.query_id))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        if self.switch_pm is not None:
            b.write(self.switch_pm.write())

        if self.switch_webview is not None:
            b.write(self.switch_webview.write())

        b.write(Vector(self.results))

        b.write(Int(self.cache_time))

        b.write(Vector(self.users))

        return b.getvalue()
