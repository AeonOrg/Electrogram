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


class SecureData(TLObject):  # type: ignore
    """Secure passport data, for more info see the passport docs »

    Constructor of :obj:`~pyrogram.raw.base.SecureData`.

    Details:
        - Layer: ``224``
        - ID: ``8AEABEC3``

    Parameters:
        data (``bytes``):
            Data

        data_hash (``bytes``):
            Data hash

        secret (``bytes``):
            Secret

    """

    __slots__: List[str] = ["data", "data_hash", "secret"]

    ID = 0x8aeabec3
    QUALNAME = "types.SecureData"

    def __init__(self, *, data: bytes, data_hash: bytes, secret: bytes) -> None:
        self.data = data  # bytes
        self.data_hash = data_hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureData":
        # No flags

        data = Bytes.read(b)

        data_hash = Bytes.read(b)

        secret = Bytes.read(b)

        return SecureData(data=data, data_hash=data_hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.data))

        b.write(Bytes(self.data_hash))

        b.write(Bytes(self.secret))

        return b.getvalue()
