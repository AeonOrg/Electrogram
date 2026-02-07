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


class MessageActionChatEditPhoto(TLObject):  # type: ignore
    """Group profile changed

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``7FCB13A8``

    Parameters:
        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            New group profile photo

    """

    __slots__: List[str] = ["photo"]

    ID = 0x7fcb13a8
    QUALNAME = "types.MessageActionChatEditPhoto"

    def __init__(self, *, photo: "raw.base.Photo") -> None:
        self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatEditPhoto":
        # No flags

        photo = TLObject.read(b)

        return MessageActionChatEditPhoto(photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.photo.write())

        return b.getvalue()
