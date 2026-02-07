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


class WebDocument(TLObject):  # type: ignore
    """Remote document

    Constructor of :obj:`~pyrogram.raw.base.WebDocument`.

    Details:
        - Layer: ``224``
        - ID: ``1C570ED1``

    Parameters:
        url (``str``):
            Document URL

        access_hash (``int`` ``64-bit``):
            Access hash

        size (``int`` ``32-bit``):
            File size

        mime_type (``str``):
            MIME type

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            Attributes for media types

    """

    __slots__: List[str] = ["url", "access_hash", "size", "mime_type", "attributes"]

    ID = 0x1c570ed1
    QUALNAME = "types.WebDocument"

    def __init__(self, *, url: str, access_hash: int, size: int, mime_type: str, attributes: List["raw.base.DocumentAttribute"]) -> None:
        self.url = url  # string
        self.access_hash = access_hash  # long
        self.size = size  # int
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebDocument":
        # No flags

        url = String.read(b)

        access_hash = Long.read(b)

        size = Int.read(b)

        mime_type = String.read(b)

        attributes = TLObject.read(b)

        return WebDocument(url=url, access_hash=access_hash, size=size, mime_type=mime_type, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Long(self.access_hash))

        b.write(Int(self.size))

        b.write(String(self.mime_type))

        b.write(Vector(self.attributes))

        return b.getvalue()
