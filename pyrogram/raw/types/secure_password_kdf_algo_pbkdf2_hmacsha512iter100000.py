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


class SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(TLObject):  # type: ignore
    """PBKDF2 with SHA512 and 100000 iterations KDF algo

    Constructor of :obj:`~pyrogram.raw.base.SecurePasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``BBF2DDA0``

    Parameters:
        salt (``bytes``):
            Salt

    """

    __slots__: List[str] = ["salt"]

    ID = 0xbbf2dda0
    QUALNAME = "types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000"

    def __init__(self, *, salt: bytes) -> None:
        self.salt = salt  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000":
        # No flags

        salt = Bytes.read(b)

        return SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000(salt=salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.salt))

        return b.getvalue()
