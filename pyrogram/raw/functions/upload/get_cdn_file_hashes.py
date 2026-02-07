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


class GetCdnFileHashes(TLObject):  # type: ignore
    """Get SHA256 hashes for verifying downloaded CDN files


    Details:
        - Layer: ``224``
        - ID: ``91DC3F31``

    Parameters:
        file_token (``bytes``):
            File

        offset (``int`` ``64-bit``):
            Offset from which to start getting hashes

    Returns:
        List of :obj:`FileHash <pyrogram.raw.base.FileHash>`
    """

    __slots__: List[str] = ["file_token", "offset"]

    ID = 0x91dc3f31
    QUALNAME = "functions.upload.GetCdnFileHashes"

    def __init__(self, *, file_token: bytes, offset: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnFileHashes":
        # No flags

        file_token = Bytes.read(b)

        offset = Long.read(b)

        return GetCdnFileHashes(file_token=file_token, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.file_token))

        b.write(Long(self.offset))

        return b.getvalue()
