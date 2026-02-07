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


class ExportLoginToken(TLObject):  # type: ignore
    """Generate a login token, for login via QR code.
The generated login token should be encoded using base64url, then shown as a tg://login?token=base64encodedtoken deep link » in the QR code.


    Details:
        - Layer: ``224``
        - ID: ``B7E085FE``

    Parameters:
        api_id (``int`` ``32-bit``):
            Application identifier (see. App configuration)

        api_hash (``str``):
            Application identifier hash (see. App configuration)

        except_ids (List of ``int`` ``64-bit``):
            List of already logged-in user IDs, to prevent logging in twice with the same user

    Returns:
        :obj:`auth.LoginToken <pyrogram.raw.base.auth.LoginToken>`
    """

    __slots__: List[str] = ["api_id", "api_hash", "except_ids"]

    ID = 0xb7e085fe
    QUALNAME = "functions.auth.ExportLoginToken"

    def __init__(self, *, api_id: int, api_hash: str, except_ids: List[int]) -> None:
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string
        self.except_ids = except_ids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportLoginToken":
        # No flags

        api_id = Int.read(b)

        api_hash = String.read(b)

        except_ids = TLObject.read(b, Long)

        return ExportLoginToken(api_id=api_id, api_hash=api_hash, except_ids=except_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.api_id))

        b.write(String(self.api_hash))

        b.write(Vector(self.except_ids, Long))

        return b.getvalue()
