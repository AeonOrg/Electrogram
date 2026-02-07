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


class InputWebDocument(TLObject):  # type: ignore
    """The document

    Constructor of :obj:`~pyrogram.raw.base.InputWebDocument`.

    Details:
        - Layer: ``224``
        - ID: ``9BED434D``

    Parameters:
        url (``str``):
            Remote document URL to be downloaded using the appropriate method

        size (``int`` ``32-bit``):
            Remote file size

        mime_type (``str``):
            Mime type

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            Attributes for media types

    """

    __slots__: List[str] = ["url", "size", "mime_type", "attributes"]

    ID = 0x9bed434d
    QUALNAME = "types.InputWebDocument"

    def __init__(self, *, url: str, size: int, mime_type: str, attributes: List["raw.base.DocumentAttribute"]) -> None:
        self.url = url  # string
        self.size = size  # int
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebDocument":
        # No flags

        url = String.read(b)

        size = Int.read(b)

        mime_type = String.read(b)

        attributes = TLObject.read(b)

        return InputWebDocument(url=url, size=size, mime_type=mime_type, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Int(self.size))

        b.write(String(self.mime_type))

        b.write(Vector(self.attributes))

        return b.getvalue()
