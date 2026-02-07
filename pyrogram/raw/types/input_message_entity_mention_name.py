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


class InputMessageEntityMentionName(TLObject):  # type: ignore
    """Message entity that can be used to create a user user mention: received mentions use the messageEntityMentionName constructor, instead.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``208E68C9``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset of message entity within message (in UTF-16 code units)

        length (``int`` ``32-bit``):
            Length of message entity within message (in UTF-16 code units)

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Identifier of the user that was mentioned

    """

    __slots__: List[str] = ["offset", "length", "user_id"]

    ID = 0x208e68c9
    QUALNAME = "types.InputMessageEntityMentionName"

    def __init__(self, *, offset: int, length: int, user_id: "raw.base.InputUser") -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageEntityMentionName":
        # No flags

        offset = Int.read(b)

        length = Int.read(b)

        user_id = TLObject.read(b)

        return InputMessageEntityMentionName(offset=offset, length=length, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.offset))

        b.write(Int(self.length))

        b.write(self.user_id.write())

        return b.getvalue()
