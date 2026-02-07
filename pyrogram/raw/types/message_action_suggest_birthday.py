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


class MessageActionSuggestBirthday(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``2C8F2A25``

    Parameters:
        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`):
            N/A

    """

    __slots__: List[str] = ["birthday"]

    ID = 0x2c8f2a25
    QUALNAME = "types.MessageActionSuggestBirthday"

    def __init__(self, *, birthday: "raw.base.Birthday") -> None:
        self.birthday = birthday  # Birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestBirthday":
        # No flags

        birthday = TLObject.read(b)

        return MessageActionSuggestBirthday(birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.birthday.write())

        return b.getvalue()
