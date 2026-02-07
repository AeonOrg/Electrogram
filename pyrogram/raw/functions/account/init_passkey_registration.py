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


class InitPasskeyRegistration(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``429547E8``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.PasskeyRegistrationOptions <pyrogram.raw.base.account.PasskeyRegistrationOptions>`
    """

    __slots__: List[str] = []

    ID = 0x429547e8
    QUALNAME = "functions.account.InitPasskeyRegistration"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitPasskeyRegistration":
        # No flags

        return InitPasskeyRegistration()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
