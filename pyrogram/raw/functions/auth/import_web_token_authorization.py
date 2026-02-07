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


class ImportWebTokenAuthorization(TLObject):  # type: ignore
    """Login by importing an authorization token


    Details:
        - Layer: ``224``
        - ID: ``2DB873A9``

    Parameters:
        api_id (``int`` ``32-bit``):
            API ID

        api_hash (``str``):
            API hash

        web_auth_token (``str``):
            The authorization token

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["api_id", "api_hash", "web_auth_token"]

    ID = 0x2db873a9
    QUALNAME = "functions.auth.ImportWebTokenAuthorization"

    def __init__(self, *, api_id: int, api_hash: str, web_auth_token: str) -> None:
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string
        self.web_auth_token = web_auth_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportWebTokenAuthorization":
        # No flags

        api_id = Int.read(b)

        api_hash = String.read(b)

        web_auth_token = String.read(b)

        return ImportWebTokenAuthorization(api_id=api_id, api_hash=api_hash, web_auth_token=web_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.api_id))

        b.write(String(self.api_hash))

        b.write(String(self.web_auth_token))

        return b.getvalue()
