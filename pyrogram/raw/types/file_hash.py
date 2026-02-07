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


class FileHash(TLObject):  # type: ignore
    """SHA256 Hash of an uploaded file, to be checked for validity after download

    Constructor of :obj:`~pyrogram.raw.base.FileHash`.

    Details:
        - Layer: ``224``
        - ID: ``F39B035C``

    Parameters:
        offset (``int`` ``64-bit``):
            Offset from where to start computing SHA-256 hash

        limit (``int`` ``32-bit``):
            Length

        hash (``bytes``):
            SHA-256 Hash of file chunk, to be checked for validity after download

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.ReuploadCdnFile
            upload.GetCdnFileHashes
            upload.GetFileHashes
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0xf39b035c
    QUALNAME = "types.FileHash"

    def __init__(self, *, offset: int, limit: int, hash: bytes) -> None:
        self.offset = offset  # long
        self.limit = limit  # int
        self.hash = hash  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileHash":
        # No flags

        offset = Long.read(b)

        limit = Int.read(b)

        hash = Bytes.read(b)

        return FileHash(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.offset))

        b.write(Int(self.limit))

        b.write(Bytes(self.hash))

        return b.getvalue()
