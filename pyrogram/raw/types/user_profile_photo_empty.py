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


class UserProfilePhotoEmpty(TLObject):  # type: ignore
    """Profile photo has not been set, or was hidden.

    Constructor of :obj:`~pyrogram.raw.base.UserProfilePhoto`.

    Details:
        - Layer: ``224``
        - ID: ``4F11BAE1``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x4f11bae1
    QUALNAME = "types.UserProfilePhotoEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserProfilePhotoEmpty":
        # No flags

        return UserProfilePhotoEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
