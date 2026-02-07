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


class RecoverPassword(TLObject):  # type: ignore
    """Reset the 2FA password using the recovery code sent using auth.requestPasswordRecovery.


    Details:
        - Layer: ``224``
        - ID: ``37096C70``

    Parameters:
        code (``str``):
            Code received via email

        new_settings (:obj:`account.PasswordInputSettings <pyrogram.raw.base.account.PasswordInputSettings>`, *optional*):
            New password

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["code", "new_settings"]

    ID = 0x37096c70
    QUALNAME = "functions.auth.RecoverPassword"

    def __init__(self, *, code: str, new_settings: "raw.base.account.PasswordInputSettings" = None) -> None:
        self.code = code  # string
        self.new_settings = new_settings  # flags.0?account.PasswordInputSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecoverPassword":

        flags = Int.read(b)

        code = String.read(b)

        new_settings = TLObject.read(b) if flags & (1 << 0) else None

        return RecoverPassword(code=code, new_settings=new_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.new_settings is not None else 0
        b.write(Int(flags))

        b.write(String(self.code))

        if self.new_settings is not None:
            b.write(self.new_settings.write())

        return b.getvalue()
