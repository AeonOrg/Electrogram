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


class PasswordSettings(TLObject):  # type: ignore
    """Private info associated to the password info (recovery email, telegram passport info & so on)

    Constructor of :obj:`~pyrogram.raw.base.account.PasswordSettings`.

    Details:
        - Layer: ``224``
        - ID: ``9A5C33E5``

    Parameters:
        email (``str``, *optional*):
            2FA Recovery email

        secure_settings (:obj:`SecureSecretSettings <pyrogram.raw.base.SecureSecretSettings>`, *optional*):
            Telegram passport settings

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPasswordSettings
    """

    __slots__: List[str] = ["email", "secure_settings"]

    ID = 0x9a5c33e5
    QUALNAME = "types.account.PasswordSettings"

    def __init__(self, *, email: Optional[str] = None, secure_settings: "raw.base.SecureSecretSettings" = None) -> None:
        self.email = email  # flags.0?string
        self.secure_settings = secure_settings  # flags.1?SecureSecretSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordSettings":

        flags = Int.read(b)

        email = String.read(b) if flags & (1 << 0) else None
        secure_settings = TLObject.read(b) if flags & (1 << 1) else None

        return PasswordSettings(email=email, secure_settings=secure_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.email is not None else 0
        flags |= (1 << 1) if self.secure_settings is not None else 0
        b.write(Int(flags))

        if self.email is not None:
            b.write(String(self.email))

        if self.secure_settings is not None:
            b.write(self.secure_settings.write())

        return b.getvalue()
