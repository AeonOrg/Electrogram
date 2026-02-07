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


class ReplyKeyboardHide(TLObject):  # type: ignore
    """Hide sent bot keyboard

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``A03E5B85``

    Parameters:
        selective (``bool``, *optional*):
            Use this flag if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet

    """

    __slots__: List[str] = ["selective"]

    ID = 0xa03e5b85
    QUALNAME = "types.ReplyKeyboardHide"

    def __init__(self, *, selective: Optional[bool] = None) -> None:
        self.selective = selective  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardHide":

        flags = Int.read(b)

        selective = True if flags & (1 << 2) else False
        return ReplyKeyboardHide(selective=selective)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.selective else 0
        b.write(Int(flags))

        return b.getvalue()
