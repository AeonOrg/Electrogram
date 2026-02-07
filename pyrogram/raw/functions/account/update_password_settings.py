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


class UpdatePasswordSettings(TLObject):  # type: ignore
    """Set a new 2FA password


    Details:
        - Layer: ``224``
        - ID: ``A59B102F``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            The old password (see SRP)

        new_settings (:obj:`account.PasswordInputSettings <pyrogram.raw.base.account.PasswordInputSettings>`):
            The new password (see SRP)

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["password", "new_settings"]

    ID = 0xa59b102f
    QUALNAME = "functions.account.UpdatePasswordSettings"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP", new_settings: "raw.base.account.PasswordInputSettings") -> None:
        self.password = password  # InputCheckPasswordSRP
        self.new_settings = new_settings  # account.PasswordInputSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePasswordSettings":
        # No flags

        password = TLObject.read(b)

        new_settings = TLObject.read(b)

        return UpdatePasswordSettings(password=password, new_settings=new_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.password.write())

        b.write(self.new_settings.write())

        return b.getvalue()
