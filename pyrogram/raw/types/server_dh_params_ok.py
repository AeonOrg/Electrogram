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


class ServerDHParamsOk(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ServerDHParams`.

    Details:
        - Layer: ``224``
        - ID: ``D0E8075C``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        encrypted_answer (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            ReqDHParams
    """

    __slots__: List[str] = ["nonce", "server_nonce", "encrypted_answer"]

    ID = 0xd0e8075c
    QUALNAME = "types.ServerDHParamsOk"

    def __init__(self, *, nonce: int, server_nonce: int, encrypted_answer: bytes) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.encrypted_answer = encrypted_answer  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ServerDHParamsOk":
        # No flags

        nonce = Int128.read(b)

        server_nonce = Int128.read(b)

        encrypted_answer = Bytes.read(b)

        return ServerDHParamsOk(nonce=nonce, server_nonce=server_nonce, encrypted_answer=encrypted_answer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int128(self.nonce))

        b.write(Int128(self.server_nonce))

        b.write(Bytes(self.encrypted_answer))

        return b.getvalue()
