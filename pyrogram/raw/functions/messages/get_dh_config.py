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


class GetDhConfig(TLObject):  # type: ignore
    """Returns configuration parameters for Diffie-Hellman key generation. Can also return a random sequence of bytes of required length.


    Details:
        - Layer: ``224``
        - ID: ``26CF8950``

    Parameters:
        version (``int`` ``32-bit``):
            Value of the version parameter from messages.dhConfig, available at the client

        random_length (``int`` ``32-bit``):
            Length of the required random sequence

    Returns:
        :obj:`messages.DhConfig <pyrogram.raw.base.messages.DhConfig>`
    """

    __slots__: List[str] = ["version", "random_length"]

    ID = 0x26cf8950
    QUALNAME = "functions.messages.GetDhConfig"

    def __init__(self, *, version: int, random_length: int) -> None:
        self.version = version  # int
        self.random_length = random_length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDhConfig":
        # No flags

        version = Int.read(b)

        random_length = Int.read(b)

        return GetDhConfig(version=version, random_length=random_length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.version))

        b.write(Int(self.random_length))

        return b.getvalue()
