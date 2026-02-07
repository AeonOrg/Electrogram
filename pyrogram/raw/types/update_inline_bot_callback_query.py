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


class UpdateInlineBotCallbackQuery(TLObject):  # type: ignore
    """This notification is received by bots when a button is pressed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``691E9052``

    Parameters:
        query_id (``int`` ``64-bit``):
            Query ID

        user_id (``int`` ``64-bit``):
            ID of the user that pressed the button

        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`):
            ID of the inline message with the button

        chat_instance (``int`` ``64-bit``):
            Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.

        data (``bytes``, *optional*):
            Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.

        game_short_name (``str``, *optional*):
            Short name of a Game to be returned, serves as the unique identifier for the game

    """

    __slots__: List[str] = ["query_id", "user_id", "msg_id", "chat_instance", "data", "game_short_name"]

    ID = 0x691e9052
    QUALNAME = "types.UpdateInlineBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, msg_id: "raw.base.InputBotInlineMessageID", chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # long
        self.msg_id = msg_id  # InputBotInlineMessageID
        self.chat_instance = chat_instance  # long
        self.data = data  # flags.0?bytes
        self.game_short_name = game_short_name  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateInlineBotCallbackQuery":

        flags = Int.read(b)

        query_id = Long.read(b)

        user_id = Long.read(b)

        msg_id = TLObject.read(b)

        chat_instance = Long.read(b)

        data = Bytes.read(b) if flags & (1 << 0) else None
        game_short_name = String.read(b) if flags & (1 << 1) else None
        return UpdateInlineBotCallbackQuery(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 1) if self.game_short_name is not None else 0
        b.write(Int(flags))

        b.write(Long(self.query_id))

        b.write(Long(self.user_id))

        b.write(self.msg_id.write())

        b.write(Long(self.chat_instance))

        if self.data is not None:
            b.write(Bytes(self.data))

        if self.game_short_name is not None:
            b.write(String(self.game_short_name))

        return b.getvalue()
