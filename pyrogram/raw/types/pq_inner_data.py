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


class PQInnerData(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PQInnerData`.

    Details:
        - Layer: ``224``
        - ID: ``83C95AEC``

    Parameters:
        pq (``bytes``):
            N/A

        p (``bytes``):
            N/A

        q (``bytes``):
            N/A

        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        new_nonce (``int`` ``256-bit``):
            N/A

    """

    __slots__: List[str] = ["pq", "p", "q", "nonce", "server_nonce", "new_nonce"]

    ID = 0x83c95aec
    QUALNAME = "types.PQInnerData"

    def __init__(self, *, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int) -> None:
        self.pq = pq  # bytes
        self.p = p  # bytes
        self.q = q  # bytes
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce = new_nonce  # int256

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PQInnerData":
        # No flags

        pq = Bytes.read(b)

        p = Bytes.read(b)

        q = Bytes.read(b)

        nonce = Int128.read(b)

        server_nonce = Int128.read(b)

        new_nonce = Int256.read(b)

        return PQInnerData(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.pq))

        b.write(Bytes(self.p))

        b.write(Bytes(self.q))

        b.write(Int128(self.nonce))

        b.write(Int128(self.server_nonce))

        b.write(Int256(self.new_nonce))

        return b.getvalue()
