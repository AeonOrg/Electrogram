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


class ReqDHParams(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D712E4BE``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        p (``bytes``):
            N/A

        q (``bytes``):
            N/A

        public_key_fingerprint (``int`` ``64-bit``):
            N/A

        encrypted_data (``bytes``):
            N/A

    Returns:
        :obj:`ServerDHParams <pyrogram.raw.base.ServerDHParams>`
    """

    __slots__: List[str] = ["nonce", "server_nonce", "p", "q", "public_key_fingerprint", "encrypted_data"]

    ID = 0xd712e4be
    QUALNAME = "functions.ReqDHParams"

    def __init__(self, *, nonce: int, server_nonce: int, p: bytes, q: bytes, public_key_fingerprint: int, encrypted_data: bytes) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.p = p  # bytes
        self.q = q  # bytes
        self.public_key_fingerprint = public_key_fingerprint  # long
        self.encrypted_data = encrypted_data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReqDHParams":
        # No flags

        nonce = Int128.read(b)

        server_nonce = Int128.read(b)

        p = Bytes.read(b)

        q = Bytes.read(b)

        public_key_fingerprint = Long.read(b)

        encrypted_data = Bytes.read(b)

        return ReqDHParams(nonce=nonce, server_nonce=server_nonce, p=p, q=q, public_key_fingerprint=public_key_fingerprint, encrypted_data=encrypted_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int128(self.nonce))

        b.write(Int128(self.server_nonce))

        b.write(Bytes(self.p))

        b.write(Bytes(self.q))

        b.write(Long(self.public_key_fingerprint))

        b.write(Bytes(self.encrypted_data))

        return b.getvalue()
