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


class GetAllSecureValues(TLObject):  # type: ignore
    """Get all saved Telegram Passport documents, for more info see the passport docs »


    Details:
        - Layer: ``224``
        - ID: ``B288BC7D``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`
    """

    __slots__: List[str] = []

    ID = 0xb288bc7d
    QUALNAME = "functions.account.GetAllSecureValues"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllSecureValues":
        # No flags

        return GetAllSecureValues()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
