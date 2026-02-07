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


class UpdateBotInlineSend(TLObject):  # type: ignore
    """The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``12F12A07``

    Parameters:
        user_id (``int`` ``64-bit``):
            The user that chose the result

        query (``str``):
            The query that was used to obtain the result

        id (``str``):
            The unique identifier for the result that was chosen

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`, *optional*):
            Optional. Sender location, only for bots that require user location

        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`, *optional*):
            Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.

    """

    __slots__: List[str] = ["user_id", "query", "id", "geo", "msg_id"]

    ID = 0x12f12a07
    QUALNAME = "types.UpdateBotInlineSend"

    def __init__(self, *, user_id: int, query: str, id: str, geo: "raw.base.GeoPoint" = None, msg_id: "raw.base.InputBotInlineMessageID" = None) -> None:
        self.user_id = user_id  # long
        self.query = query  # string
        self.id = id  # string
        self.geo = geo  # flags.0?GeoPoint
        self.msg_id = msg_id  # flags.1?InputBotInlineMessageID

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotInlineSend":

        flags = Int.read(b)

        user_id = Long.read(b)

        query = String.read(b)

        geo = TLObject.read(b) if flags & (1 << 0) else None

        id = String.read(b)

        msg_id = TLObject.read(b) if flags & (1 << 1) else None

        return UpdateBotInlineSend(user_id=user_id, query=query, id=id, geo=geo, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        b.write(Int(flags))

        b.write(Long(self.user_id))

        b.write(String(self.query))

        if self.geo is not None:
            b.write(self.geo.write())

        b.write(String(self.id))

        if self.msg_id is not None:
            b.write(self.msg_id.write())

        return b.getvalue()
