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


class UpdateUserEmojiStatus(TLObject):  # type: ignore
    """The emoji status of a certain user has changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``28373599``

    Parameters:
        user_id (``int`` ``64-bit``):
            User ID

        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            New emoji status

    """

    __slots__: List[str] = ["user_id", "emoji_status"]

    ID = 0x28373599
    QUALNAME = "types.UpdateUserEmojiStatus"

    def __init__(self, *, user_id: int, emoji_status: "raw.base.EmojiStatus") -> None:
        self.user_id = user_id  # long
        self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserEmojiStatus":
        # No flags

        user_id = Long.read(b)

        emoji_status = TLObject.read(b)

        return UpdateUserEmojiStatus(user_id=user_id, emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(self.emoji_status.write())

        return b.getvalue()
