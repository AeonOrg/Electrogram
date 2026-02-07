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


class InputPhoto(TLObject):  # type: ignore
    """Defines a photo for further interaction.

    Constructor of :obj:`~pyrogram.raw.base.InputPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``3BB3B94A``

    Parameters:
        id (``int`` ``64-bit``):
            Photo identifier

        access_hash (``int`` ``64-bit``):
            access_hash value from the photo constructor

        file_reference (``bytes``):
            File reference

    """

    __slots__: List[str] = ["id", "access_hash", "file_reference"]

    ID = 0x3bb3b94a
    QUALNAME = "types.InputPhoto"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoto":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        file_reference = Bytes.read(b)

        return InputPhoto(id=id, access_hash=access_hash, file_reference=file_reference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(Bytes(self.file_reference))

        return b.getvalue()
