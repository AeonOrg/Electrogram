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


class ReplyKeyboardForceReply(TLObject):  # type: ignore
    """Force the user to send a reply

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``86B40B08``

    Parameters:
        single_use (``bool``, *optional*):
            Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again.

        selective (``bool``, *optional*):
            Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message. Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.

        placeholder (``str``, *optional*):
            The placeholder to be shown in the input field when the keyboard is active; 1-64 characters.

    """

    __slots__: List[str] = ["single_use", "selective", "placeholder"]

    ID = 0x86b40b08
    QUALNAME = "types.ReplyKeyboardForceReply"

    def __init__(self, *, single_use: Optional[bool] = None, selective: Optional[bool] = None, placeholder: Optional[str] = None) -> None:
        self.single_use = single_use  # flags.1?true
        self.selective = selective  # flags.2?true
        self.placeholder = placeholder  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardForceReply":

        flags = Int.read(b)

        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardForceReply(single_use=single_use, selective=selective, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))

        if self.placeholder is not None:
            b.write(String(self.placeholder))

        return b.getvalue()
