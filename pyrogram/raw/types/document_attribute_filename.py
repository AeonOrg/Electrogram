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


class DocumentAttributeFilename(TLObject):  # type: ignore
    """A simple document with a file name

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``15590068``

    Parameters:
        file_name (``str``):
            The file name

    """

    __slots__: List[str] = ["file_name"]

    ID = 0x15590068
    QUALNAME = "types.DocumentAttributeFilename"

    def __init__(self, *, file_name: str) -> None:
        self.file_name = file_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeFilename":
        # No flags

        file_name = String.read(b)

        return DocumentAttributeFilename(file_name=file_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.file_name))

        return b.getvalue()
