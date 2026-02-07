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


class GetInlineBotResults(TLObject):  # type: ignore
    """Query an inline bot


    Details:
        - Layer: ``224``
        - ID: ``514E999D``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The bot to query

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The currently opened chat

        query (``str``):
            The query

        offset (``str``):
            The offset within the results, will be passed directly as-is to the bot.

        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`, *optional*):
            The geolocation, if requested

    Returns:
        :obj:`messages.BotResults <pyrogram.raw.base.messages.BotResults>`
    """

    __slots__: List[str] = ["bot", "peer", "query", "offset", "geo_point"]

    ID = 0x514e999d
    QUALNAME = "functions.messages.GetInlineBotResults"

    def __init__(self, *, bot: "raw.base.InputUser", peer: "raw.base.InputPeer", query: str, offset: str, geo_point: "raw.base.InputGeoPoint" = None) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.query = query  # string
        self.offset = offset  # string
        self.geo_point = geo_point  # flags.0?InputGeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineBotResults":

        flags = Int.read(b)

        bot = TLObject.read(b)

        peer = TLObject.read(b)

        geo_point = TLObject.read(b) if flags & (1 << 0) else None

        query = String.read(b)

        offset = String.read(b)

        return GetInlineBotResults(bot=bot, peer=peer, query=query, offset=offset, geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo_point is not None else 0
        b.write(Int(flags))

        b.write(self.bot.write())

        b.write(self.peer.write())

        if self.geo_point is not None:
            b.write(self.geo_point.write())

        b.write(String(self.query))

        b.write(String(self.offset))

        return b.getvalue()
