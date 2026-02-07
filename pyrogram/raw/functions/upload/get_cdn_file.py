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


class GetCdnFile(TLObject):  # type: ignore
    """Download a CDN file.


    Details:
        - Layer: ``224``
        - ID: ``395F69DA``

    Parameters:
        file_token (``bytes``):
            File token

        offset (``int`` ``64-bit``):
            Offset of chunk to download

        limit (``int`` ``32-bit``):
            Length of chunk to download

    Returns:
        :obj:`upload.CdnFile <pyrogram.raw.base.upload.CdnFile>`
    """

    __slots__: List[str] = ["file_token", "offset", "limit"]

    ID = 0x395f69da
    QUALNAME = "functions.upload.GetCdnFile"

    def __init__(self, *, file_token: bytes, offset: int, limit: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnFile":
        # No flags

        file_token = Bytes.read(b)

        offset = Long.read(b)

        limit = Int.read(b)

        return GetCdnFile(file_token=file_token, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.file_token))

        b.write(Long(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
