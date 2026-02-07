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


class UserInfo(TLObject):  # type: ignore
    """Internal use

    Constructor of :obj:`~pyrogram.raw.base.help.UserInfo`.

    Details:
        - Layer: ``224``
        - ID: ``1EB3758``

    Parameters:
        message (``str``):
            Info

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            Message entities for styled text

        author (``str``):
            Author

        date (``int`` ``32-bit``):
            Date

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetUserInfo
            help.EditUserInfo
    """

    __slots__: List[str] = ["message", "entities", "author", "date"]

    ID = 0x1eb3758
    QUALNAME = "types.help.UserInfo"

    def __init__(self, *, message: str, entities: List["raw.base.MessageEntity"], author: str, date: int) -> None:
        self.message = message  # string
        self.entities = entities  # Vector<MessageEntity>
        self.author = author  # string
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserInfo":
        # No flags

        message = String.read(b)

        entities = TLObject.read(b)

        author = String.read(b)

        date = Int.read(b)

        return UserInfo(message=message, entities=entities, author=author, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.message))

        b.write(Vector(self.entities))

        b.write(String(self.author))

        b.write(Int(self.date))

        return b.getvalue()
