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


class PreparedInlineMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.PreparedInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``FF57708D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        result (:obj:`BotInlineResult <pyrogram.raw.base.BotInlineResult>`):
            N/A

        peer_types (List of :obj:`InlineQueryPeerType <pyrogram.raw.base.InlineQueryPeerType>`):
            N/A

        cache_time (``int`` ``32-bit``):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPreparedInlineMessage
    """

    __slots__: List[str] = ["query_id", "result", "peer_types", "cache_time", "users"]

    ID = 0xff57708d
    QUALNAME = "types.messages.PreparedInlineMessage"

    def __init__(self, *, query_id: int, result: "raw.base.BotInlineResult", peer_types: List["raw.base.InlineQueryPeerType"], cache_time: int, users: List["raw.base.User"]) -> None:
        self.query_id = query_id  # long
        self.result = result  # BotInlineResult
        self.peer_types = peer_types  # Vector<InlineQueryPeerType>
        self.cache_time = cache_time  # int
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PreparedInlineMessage":
        # No flags

        query_id = Long.read(b)

        result = TLObject.read(b)

        peer_types = TLObject.read(b)

        cache_time = Int.read(b)

        users = TLObject.read(b)

        return PreparedInlineMessage(query_id=query_id, result=result, peer_types=peer_types, cache_time=cache_time, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        b.write(self.result.write())

        b.write(Vector(self.peer_types))

        b.write(Int(self.cache_time))

        b.write(Vector(self.users))

        return b.getvalue()
