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


class SendMessageUploadPhotoAction(TLObject):  # type: ignore
    """User is uploading a photo.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``D1D34A26``

    Parameters:
        progress (``int`` ``32-bit``):
            Progress percentage

    """

    __slots__: List[str] = ["progress"]

    ID = 0xd1d34a26
    QUALNAME = "types.SendMessageUploadPhotoAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageUploadPhotoAction":
        # No flags

        progress = Int.read(b)

        return SendMessageUploadPhotoAction(progress=progress)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.progress))

        return b.getvalue()
