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


class DhGenOk(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SetClientDHParamsAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``3BCBF734``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        new_nonce_hash1 (``int`` ``128-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            SetClientDHParams
    """

    __slots__: List[str] = ["nonce", "server_nonce", "new_nonce_hash1"]

    ID = 0x3bcbf734
    QUALNAME = "types.DhGenOk"

    def __init__(self, *, nonce: int, server_nonce: int, new_nonce_hash1: int) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce_hash1 = new_nonce_hash1  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhGenOk":
        # No flags

        nonce = Int128.read(b)

        server_nonce = Int128.read(b)

        new_nonce_hash1 = Int128.read(b)

        return DhGenOk(nonce=nonce, server_nonce=server_nonce, new_nonce_hash1=new_nonce_hash1)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int128(self.nonce))

        b.write(Int128(self.server_nonce))

        b.write(Int128(self.new_nonce_hash1))

        return b.getvalue()
