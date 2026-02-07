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


class MessageActionUserUpdatedPhoto(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``55555551``

    Parameters:
        new_user_photo (:obj:`UserProfilePhoto <pyrogram.raw.base.UserProfilePhoto>`):
            N/A

    """

    __slots__: List[str] = ["new_user_photo"]

    ID = 0x55555551
    QUALNAME = "types.MessageActionUserUpdatedPhoto"

    def __init__(self, *, new_user_photo: "raw.base.UserProfilePhoto") -> None:
        self.new_user_photo = new_user_photo  # UserProfilePhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionUserUpdatedPhoto":
        # No flags

        new_user_photo = TLObject.read(b)

        return MessageActionUserUpdatedPhoto(new_user_photo=new_user_photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.new_user_photo.write())

        return b.getvalue()
