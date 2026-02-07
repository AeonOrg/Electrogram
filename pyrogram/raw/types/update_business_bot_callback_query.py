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


class UpdateBusinessBotCallbackQuery(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1EA2FDA7``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        connection_id (``str``):
            N/A

        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        chat_instance (``int`` ``64-bit``):
            N/A

        reply_to_message (:obj:`Message <pyrogram.raw.base.Message>`, *optional*):
            N/A

        data (``bytes``, *optional*):
            N/A

    """

    __slots__: List[str] = ["query_id", "user_id", "connection_id", "message", "chat_instance", "reply_to_message", "data"]

    ID = 0x1ea2fda7
    QUALNAME = "types.UpdateBusinessBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, connection_id: str, message: "raw.base.Message", chat_instance: int, reply_to_message: "raw.base.Message" = None, data: Optional[bytes] = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # long
        self.connection_id = connection_id  # string
        self.message = message  # Message
        self.chat_instance = chat_instance  # long
        self.reply_to_message = reply_to_message  # flags.2?Message
        self.data = data  # flags.0?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessBotCallbackQuery":

        flags = Int.read(b)

        query_id = Long.read(b)

        user_id = Long.read(b)

        connection_id = String.read(b)

        message = TLObject.read(b)

        reply_to_message = TLObject.read(b) if flags & (1 << 2) else None

        chat_instance = Long.read(b)

        data = Bytes.read(b) if flags & (1 << 0) else None
        return UpdateBusinessBotCallbackQuery(query_id=query_id, user_id=user_id, connection_id=connection_id, message=message, chat_instance=chat_instance, reply_to_message=reply_to_message, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_to_message is not None else 0
        flags |= (1 << 0) if self.data is not None else 0
        b.write(Int(flags))

        b.write(Long(self.query_id))

        b.write(Long(self.user_id))

        b.write(String(self.connection_id))

        b.write(self.message.write())

        if self.reply_to_message is not None:
            b.write(self.reply_to_message.write())

        b.write(Long(self.chat_instance))

        if self.data is not None:
            b.write(Bytes(self.data))

        return b.getvalue()
