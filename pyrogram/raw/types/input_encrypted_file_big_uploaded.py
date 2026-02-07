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


class InputEncryptedFileBigUploaded(TLObject):  # type: ignore
    """Assigns a new big encrypted file (over 10 MB in size), saved in parts using the method upload.saveBigFilePart.

    Constructor of :obj:`~pyrogram.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``2DC173C8``

    Parameters:
        id (``int`` ``64-bit``):
            Random file id, created by the client

        parts (``int`` ``32-bit``):
            Number of saved parts

        key_fingerprint (``int`` ``32-bit``):
            32-bit imprint of the key used to encrypt the file

    """

    __slots__: List[str] = ["id", "parts", "key_fingerprint"]

    ID = 0x2dc173c8
    QUALNAME = "types.InputEncryptedFileBigUploaded"

    def __init__(self, *, id: int, parts: int, key_fingerprint: int) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedFileBigUploaded":
        # No flags

        id = Long.read(b)

        parts = Int.read(b)

        key_fingerprint = Int.read(b)

        return InputEncryptedFileBigUploaded(id=id, parts=parts, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Int(self.parts))

        b.write(Int(self.key_fingerprint))

        return b.getvalue()
