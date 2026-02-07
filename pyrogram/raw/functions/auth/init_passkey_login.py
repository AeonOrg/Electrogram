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


class InitPasskeyLogin(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``518AD0B7``

    Parameters:
        api_id (``int`` ``32-bit``):
            N/A

        api_hash (``str``):
            N/A

    Returns:
        :obj:`auth.PasskeyLoginOptions <pyrogram.raw.base.auth.PasskeyLoginOptions>`
    """

    __slots__: List[str] = ["api_id", "api_hash"]

    ID = 0x518ad0b7
    QUALNAME = "functions.auth.InitPasskeyLogin"

    def __init__(self, *, api_id: int, api_hash: str) -> None:
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitPasskeyLogin":
        # No flags

        api_id = Int.read(b)

        api_hash = String.read(b)

        return InitPasskeyLogin(api_id=api_id, api_hash=api_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.api_id))

        b.write(String(self.api_hash))

        return b.getvalue()
