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


class InputMediaPhotoExternal(TLObject):  # type: ignore
    """New photo that will be uploaded by the server using the specified URL

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``E5BBFE1A``

    Parameters:
        url (``str``):
            URL of the photo

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Self-destruct time to live of photo

    """

    __slots__: List[str] = ["url", "spoiler", "ttl_seconds"]

    ID = 0xe5bbfe1a
    QUALNAME = "types.InputMediaPhotoExternal"

    def __init__(self, *, url: str, spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None) -> None:
        self.url = url  # string
        self.spoiler = spoiler  # flags.1?true
        self.ttl_seconds = ttl_seconds  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPhotoExternal":

        flags = Int.read(b)

        spoiler = True if flags & (1 << 1) else False
        url = String.read(b)

        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        return InputMediaPhotoExternal(url=url, spoiler=spoiler, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        b.write(Int(flags))

        b.write(String(self.url))

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        return b.getvalue()
