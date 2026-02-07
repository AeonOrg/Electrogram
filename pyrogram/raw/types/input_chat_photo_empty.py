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


class InputChatPhotoEmpty(TLObject):  # type: ignore
    """Empty constructor, remove group photo.

    Constructor of :obj:`~pyrogram.raw.base.InputChatPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``1CA48F57``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x1ca48f57
    QUALNAME = "types.InputChatPhotoEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatPhotoEmpty":
        # No flags

        return InputChatPhotoEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
