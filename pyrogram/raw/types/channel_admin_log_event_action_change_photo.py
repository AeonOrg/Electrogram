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


class ChannelAdminLogEventActionChangePhoto(TLObject):  # type: ignore
    """The channel/supergroup's picture was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``434BD2AF``

    Parameters:
        prev_photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            Previous picture

        new_photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            New picture

    """

    __slots__: List[str] = ["prev_photo", "new_photo"]

    ID = 0x434bd2af
    QUALNAME = "types.ChannelAdminLogEventActionChangePhoto"

    def __init__(self, *, prev_photo: "raw.base.Photo", new_photo: "raw.base.Photo") -> None:
        self.prev_photo = prev_photo  # Photo
        self.new_photo = new_photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangePhoto":
        # No flags

        prev_photo = TLObject.read(b)

        new_photo = TLObject.read(b)

        return ChannelAdminLogEventActionChangePhoto(prev_photo=prev_photo, new_photo=new_photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_photo.write())

        b.write(self.new_photo.write())

        return b.getvalue()
