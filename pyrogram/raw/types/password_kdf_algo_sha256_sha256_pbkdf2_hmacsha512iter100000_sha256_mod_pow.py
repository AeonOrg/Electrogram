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


class PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(TLObject):  # type: ignore
    """This key derivation algorithm defines that SRP 2FA login must be used

    Constructor of :obj:`~pyrogram.raw.base.PasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``3A912D4A``

    Parameters:
        salt1 (``bytes``):
            One of two salts used by the derivation function (see SRP 2FA login)

        salt2 (``bytes``):
            One of two salts used by the derivation function (see SRP 2FA login)

        g (``int`` ``32-bit``):
            Base (see SRP 2FA login)

        p (``bytes``):
            2048-bit modulus (see SRP 2FA login)

    """

    __slots__: List[str] = ["salt1", "salt2", "g", "p"]

    ID = 0x3a912d4a
    QUALNAME = "types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"

    def __init__(self, *, salt1: bytes, salt2: bytes, g: int, p: bytes) -> None:
        self.salt1 = salt1  # bytes
        self.salt2 = salt2  # bytes
        self.g = g  # int
        self.p = p  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow":
        # No flags

        salt1 = Bytes.read(b)

        salt2 = Bytes.read(b)

        g = Int.read(b)

        p = Bytes.read(b)

        return PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow(salt1=salt1, salt2=salt2, g=g, p=p)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.salt1))

        b.write(Bytes(self.salt2))

        b.write(Int(self.g))

        b.write(Bytes(self.p))

        return b.getvalue()
