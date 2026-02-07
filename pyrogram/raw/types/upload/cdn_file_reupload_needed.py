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


class CdnFileReuploadNeeded(TLObject):  # type: ignore
    """The file was cleared from the temporary RAM cache of the CDN and has to be re-uploaded.

    Constructor of :obj:`~pyrogram.raw.base.upload.CdnFile`.

    Details:
        - Layer: ``224``
        - ID: ``EEA8E46E``

    Parameters:
        request_token (``bytes``):
            Request token (see CDN)

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetCdnFile
    """

    __slots__: List[str] = ["request_token"]

    ID = 0xeea8e46e
    QUALNAME = "types.upload.CdnFileReuploadNeeded"

    def __init__(self, *, request_token: bytes) -> None:
        self.request_token = request_token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnFileReuploadNeeded":
        # No flags

        request_token = Bytes.read(b)

        return CdnFileReuploadNeeded(request_token=request_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.request_token))

        return b.getvalue()
