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


class SaveBigFilePart(TLObject):  # type: ignore
    """Saves a part of a large file (over 10 MB in size) to be later passed to one of the methods.


    Details:
        - Layer: ``224``
        - ID: ``DE7B673D``

    Parameters:
        file_id (``int`` ``64-bit``):
            Random file id, created by the client

        file_part (``int`` ``32-bit``):
            Part sequence number

        file_total_parts (``int`` ``32-bit``):
            Total number of parts

        bytes (``bytes``):
            Binary data, part contents

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["file_id", "file_part", "file_total_parts", "bytes"]

    ID = 0xde7b673d
    QUALNAME = "functions.upload.SaveBigFilePart"

    def __init__(self, *, file_id: int, file_part: int, file_total_parts: int, bytes: bytes) -> None:
        self.file_id = file_id  # long
        self.file_part = file_part  # int
        self.file_total_parts = file_total_parts  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveBigFilePart":
        # No flags

        file_id = Long.read(b)

        file_part = Int.read(b)

        file_total_parts = Int.read(b)

        bytes = Bytes.read(b)

        return SaveBigFilePart(file_id=file_id, file_part=file_part, file_total_parts=file_total_parts, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.file_id))

        b.write(Int(self.file_part))

        b.write(Int(self.file_total_parts))

        b.write(Bytes(self.bytes))

        return b.getvalue()
