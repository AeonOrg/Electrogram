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


class FileCdnRedirect(TLObject):  # type: ignore
    """The file must be downloaded from a CDN DC.

    Constructor of :obj:`~pyrogram.raw.base.upload.File`.

    Details:
        - Layer: ``224``
        - ID: ``F18CDA44``

    Parameters:
        dc_id (``int`` ``32-bit``):
            CDN DC ID

        file_token (``bytes``):
            File token (see CDN files)

        encryption_key (``bytes``):
            Encryption key (see CDN files)

        encryption_iv (``bytes``):
            Encryption IV (see CDN files)

        file_hashes (List of :obj:`FileHash <pyrogram.raw.base.FileHash>`):
            File hashes (see CDN files)

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetFile
    """

    __slots__: List[str] = ["dc_id", "file_token", "encryption_key", "encryption_iv", "file_hashes"]

    ID = 0xf18cda44
    QUALNAME = "types.upload.FileCdnRedirect"

    def __init__(self, *, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes, file_hashes: List["raw.base.FileHash"]) -> None:
        self.dc_id = dc_id  # int
        self.file_token = file_token  # bytes
        self.encryption_key = encryption_key  # bytes
        self.encryption_iv = encryption_iv  # bytes
        self.file_hashes = file_hashes  # Vector<FileHash>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileCdnRedirect":
        # No flags

        dc_id = Int.read(b)

        file_token = Bytes.read(b)

        encryption_key = Bytes.read(b)

        encryption_iv = Bytes.read(b)

        file_hashes = TLObject.read(b)

        return FileCdnRedirect(dc_id=dc_id, file_token=file_token, encryption_key=encryption_key, encryption_iv=encryption_iv, file_hashes=file_hashes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.dc_id))

        b.write(Bytes(self.file_token))

        b.write(Bytes(self.encryption_key))

        b.write(Bytes(self.encryption_iv))

        b.write(Vector(self.file_hashes))

        return b.getvalue()
