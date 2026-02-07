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


class GetFile(TLObject):  # type: ignore
    """Returns content of a whole file or its part.


    Details:
        - Layer: ``224``
        - ID: ``BE5335BE``

    Parameters:
        location (:obj:`InputFileLocation <pyrogram.raw.base.InputFileLocation>`):
            File location

        offset (``int`` ``64-bit``):
            Number of bytes to be skipped

        limit (``int`` ``32-bit``):
            Number of bytes to be returned

        precise (``bool``, *optional*):
            Disable some checks on limit and offset values, useful for example to stream videos by keyframes

        cdn_supported (``bool``, *optional*):
            Whether the current client supports CDN downloads

    Returns:
        :obj:`upload.File <pyrogram.raw.base.upload.File>`
    """

    __slots__: List[str] = ["location", "offset", "limit", "precise", "cdn_supported"]

    ID = 0xbe5335be
    QUALNAME = "functions.upload.GetFile"

    def __init__(self, *, location: "raw.base.InputFileLocation", offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None) -> None:
        self.location = location  # InputFileLocation
        self.offset = offset  # long
        self.limit = limit  # int
        self.precise = precise  # flags.0?true
        self.cdn_supported = cdn_supported  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFile":

        flags = Int.read(b)

        precise = True if flags & (1 << 0) else False
        cdn_supported = True if flags & (1 << 1) else False
        location = TLObject.read(b)

        offset = Long.read(b)

        limit = Int.read(b)

        return GetFile(location=location, offset=offset, limit=limit, precise=precise, cdn_supported=cdn_supported)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.precise else 0
        flags |= (1 << 1) if self.cdn_supported else 0
        b.write(Int(flags))

        b.write(self.location.write())

        b.write(Long(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
