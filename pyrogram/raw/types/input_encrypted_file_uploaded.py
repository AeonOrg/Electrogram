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


class InputEncryptedFileUploaded(TLObject):  # type: ignore
    """Sets new encrypted file saved by parts using upload.saveFilePart method.

    Constructor of :obj:`~pyrogram.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``64BD0306``

    Parameters:
        id (``int`` ``64-bit``):
            Random file ID created by client

        parts (``int`` ``32-bit``):
            Number of saved parts

        md5_checksum (``str``):
            In case md5-HASH of the (already encrypted) file was transmitted, file content will be checked prior to use

        key_fingerprint (``int`` ``32-bit``):
            32-bit fingerprint of the key used to encrypt a file

    """

    __slots__: List[str] = ["id", "parts", "md5_checksum", "key_fingerprint"]

    ID = 0x64bd0306
    QUALNAME = "types.InputEncryptedFileUploaded"

    def __init__(self, *, id: int, parts: int, md5_checksum: str, key_fingerprint: int) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.md5_checksum = md5_checksum  # string
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedFileUploaded":
        # No flags

        id = Long.read(b)

        parts = Int.read(b)

        md5_checksum = String.read(b)

        key_fingerprint = Int.read(b)

        return InputEncryptedFileUploaded(id=id, parts=parts, md5_checksum=md5_checksum, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Int(self.parts))

        b.write(String(self.md5_checksum))

        b.write(Int(self.key_fingerprint))

        return b.getvalue()
