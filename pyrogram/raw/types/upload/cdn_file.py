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


class CdnFile(TLObject):  # type: ignore
    """Represent a chunk of a CDN file.

    Constructor of :obj:`~pyrogram.raw.base.upload.CdnFile`.

    Details:
        - Layer: ``224``
        - ID: ``A99FCA4F``

    Parameters:
        bytes (``bytes``):
            The data

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetCdnFile
    """

    __slots__: List[str] = ["bytes"]

    ID = 0xa99fca4f
    QUALNAME = "types.upload.CdnFile"

    def __init__(self, *, bytes: bytes) -> None:
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnFile":
        # No flags

        bytes = Bytes.read(b)

        return CdnFile(bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.bytes))

        return b.getvalue()
