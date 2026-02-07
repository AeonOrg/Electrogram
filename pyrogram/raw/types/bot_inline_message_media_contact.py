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


class BotInlineMessageMediaContact(TLObject):  # type: ignore
    """Send a contact

    Constructor of :obj:`~pyrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``18D1CDC2``

    Parameters:
        phone_number (``str``):
            Phone number

        first_name (``str``):
            First name

        last_name (``str``):
            Last name

        vcard (``str``):
            VCard info

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["phone_number", "first_name", "last_name", "vcard", "reply_markup"]

    ID = 0x18d1cdc2
    QUALNAME = "types.BotInlineMessageMediaContact"

    def __init__(self, *, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.phone_number = phone_number  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.vcard = vcard  # string
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaContact":

        flags = Int.read(b)

        phone_number = String.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        vcard = String.read(b)

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return BotInlineMessageMediaContact(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))

        b.write(String(self.phone_number))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        b.write(String(self.vcard))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        return b.getvalue()
