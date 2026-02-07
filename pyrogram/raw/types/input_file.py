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


class InputFile(TLObject):  # type: ignore
    """Defines a file saved in parts using the method upload.saveFilePart.

    Constructor of :obj:`~pyrogram.raw.base.InputFile`.

    Details:
        - Layer: ``224``
        - ID: ``F52FF27F``

    Parameters:
        id (``int`` ``64-bit``):
            Random file identifier created by the client

        parts (``int`` ``32-bit``):
            Number of parts saved

        name (``str``):
            Full name of the file

        md5_checksum (``str``):
            In case the file's md5-hash was passed, contents of the file will be checked prior to use

    """

    __slots__: List[str] = ["id", "parts", "name", "md5_checksum"]

    ID = 0xf52ff27f
    QUALNAME = "types.InputFile"

    def __init__(self, *, id: int, parts: int, name: str, md5_checksum: str) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.name = name  # string
        self.md5_checksum = md5_checksum  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFile":
        # No flags

        id = Long.read(b)

        parts = Int.read(b)

        name = String.read(b)

        md5_checksum = String.read(b)

        return InputFile(id=id, parts=parts, name=name, md5_checksum=md5_checksum)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Int(self.parts))

        b.write(String(self.name))

        b.write(String(self.md5_checksum))

        return b.getvalue()
