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


class UpdateProfilePhoto(TLObject):  # type: ignore
    """Installs a previously uploaded photo as a profile photo.


    Details:
        - Layer: ``224``
        - ID: ``9E82039``

    Parameters:
        id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            Input photo

        fallback (``bool``, *optional*):
            If set, the chosen profile photo will be shown to users that can't display your main profile photo due to your privacy settings.

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            Can contain info of a bot we own, to change the profile photo of that bot, instead of the current user.

    Returns:
        :obj:`photos.Photo <pyrogram.raw.base.photos.Photo>`
    """

    __slots__: List[str] = ["id", "fallback", "bot"]

    ID = 0x9e82039
    QUALNAME = "functions.photos.UpdateProfilePhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", fallback: Optional[bool] = None, bot: "raw.base.InputUser" = None) -> None:
        self.id = id  # InputPhoto
        self.fallback = fallback  # flags.0?true
        self.bot = bot  # flags.1?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateProfilePhoto":

        flags = Int.read(b)

        fallback = True if flags & (1 << 0) else False
        bot = TLObject.read(b) if flags & (1 << 1) else None

        id = TLObject.read(b)

        return UpdateProfilePhoto(id=id, fallback=fallback, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fallback else 0
        flags |= (1 << 1) if self.bot is not None else 0
        b.write(Int(flags))

        if self.bot is not None:
            b.write(self.bot.write())

        b.write(self.id.write())

        return b.getvalue()
