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


class MessageActionSuggestProfilePhoto(TLObject):  # type: ignore
    """A new profile picture was suggested using photos.uploadContactProfilePhoto.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``57DE635E``

    Parameters:
        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            The photo that the user suggested we set as profile picture.

    """

    __slots__: List[str] = ["photo"]

    ID = 0x57de635e
    QUALNAME = "types.MessageActionSuggestProfilePhoto"

    def __init__(self, *, photo: "raw.base.Photo") -> None:
        self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestProfilePhoto":
        # No flags

        photo = TLObject.read(b)

        return MessageActionSuggestProfilePhoto(photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.photo.write())

        return b.getvalue()
