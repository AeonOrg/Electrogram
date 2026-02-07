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


class GetWebViewResult(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``22B6C214``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`messages.WebViewResult <pyrogram.raw.base.messages.WebViewResult>`
    """

    __slots__: List[str] = ["peer", "bot", "query_id"]

    ID = 0x22b6c214
    QUALNAME = "functions.messages.GetWebViewResult"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", query_id: int) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebViewResult":
        # No flags

        peer = TLObject.read(b)

        bot = TLObject.read(b)

        query_id = Long.read(b)

        return GetWebViewResult(peer=peer, bot=bot, query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.bot.write())

        b.write(Long(self.query_id))

        return b.getvalue()
