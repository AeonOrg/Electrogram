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


class GetFileHashes(TLObject):  # type: ignore
    """Get SHA256 hashes for verifying downloaded files


    Details:
        - Layer: ``224``
        - ID: ``9156982A``

    Parameters:
        location (:obj:`InputFileLocation <pyrogram.raw.base.InputFileLocation>`):
            File

        offset (``int`` ``64-bit``):
            Offset from which to get file hashes

    Returns:
        List of :obj:`FileHash <pyrogram.raw.base.FileHash>`
    """

    __slots__: List[str] = ["location", "offset"]

    ID = 0x9156982a
    QUALNAME = "functions.upload.GetFileHashes"

    def __init__(self, *, location: "raw.base.InputFileLocation", offset: int) -> None:
        self.location = location  # InputFileLocation
        self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFileHashes":
        # No flags

        location = TLObject.read(b)

        offset = Long.read(b)

        return GetFileHashes(location=location, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.location.write())

        b.write(Long(self.offset))

        return b.getvalue()
