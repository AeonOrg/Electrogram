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


class SecurePasswordKdfAlgoSHA512(TLObject):  # type: ignore
    """SHA512 KDF algo

    Constructor of :obj:`~pyrogram.raw.base.SecurePasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``86471D92``

    Parameters:
        salt (``bytes``):
            Salt

    """

    __slots__: List[str] = ["salt"]

    ID = 0x86471d92
    QUALNAME = "types.SecurePasswordKdfAlgoSHA512"

    def __init__(self, *, salt: bytes) -> None:
        self.salt = salt  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePasswordKdfAlgoSHA512":
        # No flags

        salt = Bytes.read(b)

        return SecurePasswordKdfAlgoSHA512(salt=salt)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.salt))

        return b.getvalue()
