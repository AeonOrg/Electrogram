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


class InputFileBig(TLObject):  # type: ignore
    """Assigns a big file (over 10 MB in size), saved in part using the method upload.saveBigFilePart.

    Constructor of :obj:`~pyrogram.raw.base.InputFile`.

    Details:
        - Layer: ``224``
        - ID: ``FA4F0BB5``

    Parameters:
        id (``int`` ``64-bit``):
            Random file id, created by the client

        parts (``int`` ``32-bit``):
            Number of parts saved

        name (``str``):
            Full file name

    """

    __slots__: List[str] = ["id", "parts", "name"]

    ID = 0xfa4f0bb5
    QUALNAME = "types.InputFileBig"

    def __init__(self, *, id: int, parts: int, name: str) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFileBig":
        # No flags

        id = Long.read(b)

        parts = Int.read(b)

        name = String.read(b)

        return InputFileBig(id=id, parts=parts, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Int(self.parts))

        b.write(String(self.name))

        return b.getvalue()
