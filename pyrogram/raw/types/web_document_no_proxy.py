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


class WebDocumentNoProxy(TLObject):  # type: ignore
    """Remote document that can be downloaded without proxying through telegram

    Constructor of :obj:`~pyrogram.raw.base.WebDocument`.

    Details:
        - Layer: ``224``
        - ID: ``F9C8BCC6``

    Parameters:
        url (``str``):
            Document URL

        size (``int`` ``32-bit``):
            File size

        mime_type (``str``):
            MIME type

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            Attributes for media types

    """

    __slots__: List[str] = ["url", "size", "mime_type", "attributes"]

    ID = 0xf9c8bcc6
    QUALNAME = "types.WebDocumentNoProxy"

    def __init__(self, *, url: str, size: int, mime_type: str, attributes: List["raw.base.DocumentAttribute"]) -> None:
        self.url = url  # string
        self.size = size  # int
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebDocumentNoProxy":
        # No flags

        url = String.read(b)

        size = Int.read(b)

        mime_type = String.read(b)

        attributes = TLObject.read(b)

        return WebDocumentNoProxy(url=url, size=size, mime_type=mime_type, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Int(self.size))

        b.write(String(self.mime_type))

        b.write(Vector(self.attributes))

        return b.getvalue()
