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


class EncryptedFileEmpty(TLObject):  # type: ignore
    """Empty constructor, non-existing file.

    Constructor of :obj:`~pyrogram.raw.base.EncryptedFile`.

    Details:
        - Layer: ``224``
        - ID: ``C21F497E``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadEncryptedFile
    """

    __slots__: List[str] = []

    ID = 0xc21f497e
    QUALNAME = "types.EncryptedFileEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedFileEmpty":
        # No flags

        return EncryptedFileEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
