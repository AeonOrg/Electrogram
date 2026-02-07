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


class MessageMediaPhoto(TLObject):  # type: ignore
    """Attached photo.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``695150D7``

    Parameters:
        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Photo

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live in seconds of self-destructing photo

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["spoiler", "photo", "ttl_seconds"]

    ID = 0x695150d7
    QUALNAME = "types.MessageMediaPhoto"

    def __init__(self, *, spoiler: Optional[bool] = None, photo: "raw.base.Photo" = None, ttl_seconds: Optional[int] = None) -> None:
        self.spoiler = spoiler  # flags.3?true
        self.photo = photo  # flags.0?Photo
        self.ttl_seconds = ttl_seconds  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaPhoto":

        flags = Int.read(b)

        spoiler = True if flags & (1 << 3) else False
        photo = TLObject.read(b) if flags & (1 << 0) else None

        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        return MessageMediaPhoto(spoiler=spoiler, photo=photo, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.spoiler else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.ttl_seconds is not None else 0
        b.write(Int(flags))

        if self.photo is not None:
            b.write(self.photo.write())

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        return b.getvalue()
