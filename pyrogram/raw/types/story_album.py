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


class StoryAlbum(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StoryAlbum`.

    Details:
        - Layer: ``224``
        - ID: ``9325705A``

    Parameters:
        album_id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        icon_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        icon_video (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CreateAlbum
            stories.UpdateAlbum
    """

    __slots__: List[str] = ["album_id", "title", "icon_photo", "icon_video"]

    ID = 0x9325705a
    QUALNAME = "types.StoryAlbum"

    def __init__(self, *, album_id: int, title: str, icon_photo: "raw.base.Photo" = None, icon_video: "raw.base.Document" = None) -> None:
        self.album_id = album_id  # int
        self.title = title  # string
        self.icon_photo = icon_photo  # flags.0?Photo
        self.icon_video = icon_video  # flags.1?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryAlbum":

        flags = Int.read(b)

        album_id = Int.read(b)

        title = String.read(b)

        icon_photo = TLObject.read(b) if flags & (1 << 0) else None

        icon_video = TLObject.read(b) if flags & (1 << 1) else None

        return StoryAlbum(album_id=album_id, title=title, icon_photo=icon_photo, icon_video=icon_video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.icon_photo is not None else 0
        flags |= (1 << 1) if self.icon_video is not None else 0
        b.write(Int(flags))

        b.write(Int(self.album_id))

        b.write(String(self.title))

        if self.icon_photo is not None:
            b.write(self.icon_photo.write())

        if self.icon_video is not None:
            b.write(self.icon_video.write())

        return b.getvalue()
