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


class CheckPassword(TLObject):  # type: ignore
    """Try logging to an account protected by a 2FA password.


    Details:
        - Layer: ``224``
        - ID: ``D18B4D16``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            The account's password (see SRP)

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["password"]

    ID = 0xd18b4d16
    QUALNAME = "functions.auth.CheckPassword"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP") -> None:
        self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckPassword":
        # No flags

        password = TLObject.read(b)

        return CheckPassword(password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.password.write())

        return b.getvalue()
