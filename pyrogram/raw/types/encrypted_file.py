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


class EncryptedFile(TLObject):  # type: ignore
    """Encrypted file.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``A8008CD8``

    Parameters:
        id (``int`` ``64-bit``):
            File ID

        access_hash (``int`` ``64-bit``):
            Checking sum depending on user ID

        size (``int`` ``64-bit``):
            File size in bytes

        dc_id (``int`` ``32-bit``):
            Number of data center

        key_fingerprint (``int`` ``32-bit``):
            32-bit fingerprint of key used for file encryption

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadEncryptedFile
    """

    __slots__: List[str] = ["id", "access_hash", "size", "dc_id", "key_fingerprint"]

    ID = 0xa8008cd8
    QUALNAME = "types.EncryptedFile"

    def __init__(self, *, id: int, access_hash: int, size: int, dc_id: int, key_fingerprint: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.size = size  # long
        self.dc_id = dc_id  # int
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedFile":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        size = Long.read(b)

        dc_id = Int.read(b)

        key_fingerprint = Int.read(b)

        return EncryptedFile(id=id, access_hash=access_hash, size=size, dc_id=dc_id, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(Long(self.size))

        b.write(Int(self.dc_id))

        b.write(Int(self.key_fingerprint))

        return b.getvalue()
