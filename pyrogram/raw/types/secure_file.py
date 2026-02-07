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


class SecureFile(TLObject):  # type: ignore
    """Secure passport file, for more info see the passport docs »

    Constructor of :obj:`~pyrogram.raw.base.SecureFile`.

    Details:
        - Layer: ``224``
        - ID: ``7D09C27E``

    Parameters:
        id (``int`` ``64-bit``):
            ID

        access_hash (``int`` ``64-bit``):
            Access hash

        size (``int`` ``64-bit``):
            File size

        dc_id (``int`` ``32-bit``):
            DC ID

        date (``int`` ``32-bit``):
            Date of upload

        file_hash (``bytes``):
            File hash

        secret (``bytes``):
            Secret

    """

    __slots__: List[str] = ["id", "access_hash", "size", "dc_id", "date", "file_hash", "secret"]

    ID = 0x7d09c27e
    QUALNAME = "types.SecureFile"

    def __init__(self, *, id: int, access_hash: int, size: int, dc_id: int, date: int, file_hash: bytes, secret: bytes) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.size = size  # long
        self.dc_id = dc_id  # int
        self.date = date  # int
        self.file_hash = file_hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureFile":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        size = Long.read(b)

        dc_id = Int.read(b)

        date = Int.read(b)

        file_hash = Bytes.read(b)

        secret = Bytes.read(b)

        return SecureFile(id=id, access_hash=access_hash, size=size, dc_id=dc_id, date=date, file_hash=file_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(Long(self.size))

        b.write(Int(self.dc_id))

        b.write(Int(self.date))

        b.write(Bytes(self.file_hash))

        b.write(Bytes(self.secret))

        return b.getvalue()
