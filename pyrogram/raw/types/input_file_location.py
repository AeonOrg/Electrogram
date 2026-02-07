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


class InputFileLocation(TLObject):  # type: ignore
    """DEPRECATED location of a photo

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``DFDAABE1``

    Parameters:
        volume_id (``int`` ``64-bit``):
            Server volume

        local_id (``int`` ``32-bit``):
            File identifier

        secret (``int`` ``64-bit``):
            Check sum to access the file

        file_reference (``bytes``):
            File reference

    """

    __slots__: List[str] = ["volume_id", "local_id", "secret", "file_reference"]

    ID = 0xdfdaabe1
    QUALNAME = "types.InputFileLocation"

    def __init__(self, *, volume_id: int, local_id: int, secret: int, file_reference: bytes) -> None:
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int
        self.secret = secret  # long
        self.file_reference = file_reference  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFileLocation":
        # No flags

        volume_id = Long.read(b)

        local_id = Int.read(b)

        secret = Long.read(b)

        file_reference = Bytes.read(b)

        return InputFileLocation(volume_id=volume_id, local_id=local_id, secret=secret, file_reference=file_reference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.volume_id))

        b.write(Int(self.local_id))

        b.write(Long(self.secret))

        b.write(Bytes(self.file_reference))

        return b.getvalue()
