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


class InputSecureFileUploaded(TLObject):  # type: ignore
    """Uploaded secure file, for more info see the passport docs »

    Constructor of :obj:`~pyrogram.raw.base.InputSecureFile`.

    Details:
        - Layer: ``224``
        - ID: ``3334B0F0``

    Parameters:
        id (``int`` ``64-bit``):
            Secure file ID

        parts (``int`` ``32-bit``):
            Secure file part count

        md5_checksum (``str``):
            MD5 hash of encrypted uploaded file, to be checked server-side

        file_hash (``bytes``):
            File hash

        secret (``bytes``):
            Secret

    """

    __slots__: List[str] = ["id", "parts", "md5_checksum", "file_hash", "secret"]

    ID = 0x3334b0f0
    QUALNAME = "types.InputSecureFileUploaded"

    def __init__(self, *, id: int, parts: int, md5_checksum: str, file_hash: bytes, secret: bytes) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.md5_checksum = md5_checksum  # string
        self.file_hash = file_hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSecureFileUploaded":
        # No flags

        id = Long.read(b)

        parts = Int.read(b)

        md5_checksum = String.read(b)

        file_hash = Bytes.read(b)

        secret = Bytes.read(b)

        return InputSecureFileUploaded(id=id, parts=parts, md5_checksum=md5_checksum, file_hash=file_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Int(self.parts))

        b.write(String(self.md5_checksum))

        b.write(Bytes(self.file_hash))

        b.write(Bytes(self.secret))

        return b.getvalue()
