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


class InputBotInlineMessageMediaAuto(TLObject):  # type: ignore
    """A media

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``3380C786``

    Parameters:
        message (``str``):
            Caption

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["message", "invert_media", "entities", "reply_markup"]

    ID = 0x3380c786
    QUALNAME = "types.InputBotInlineMessageMediaAuto"

    def __init__(self, *, message: str, invert_media: Optional[bool] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.message = message  # string
        self.invert_media = invert_media  # flags.3?true
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaAuto":

        flags = Int.read(b)

        invert_media = True if flags & (1 << 3) else False
        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 1) else []

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return InputBotInlineMessageMediaAuto(message=message, invert_media=invert_media, entities=entities, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.invert_media else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        return b.getvalue()
