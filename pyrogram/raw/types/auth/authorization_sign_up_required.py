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


class AuthorizationSignUpRequired(TLObject):  # type: ignore
    """An account with this phone number doesn't exist on telegram: the user has to enter basic information and sign up

    Constructor of :obj:`~pyrogram.raw.base.auth.Authorization`.

    Details:
        - Layer: ``224``
        - ID: ``44747E9A``

    Parameters:
        terms_of_service (:obj:`help.TermsOfService <pyrogram.raw.base.help.TermsOfService>`, *optional*):
            Telegram's terms of service: the user must read and accept the terms of service before signing up to telegram

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SignUp
            auth.SignIn
            auth.ImportAuthorization
            auth.ImportBotAuthorization
            auth.CheckPassword
            auth.RecoverPassword
            auth.ImportWebTokenAuthorization
            auth.FinishPasskeyLogin
    """

    __slots__: List[str] = ["terms_of_service"]

    ID = 0x44747e9a
    QUALNAME = "types.auth.AuthorizationSignUpRequired"

    def __init__(self, *, terms_of_service: "raw.base.help.TermsOfService" = None) -> None:
        self.terms_of_service = terms_of_service  # flags.0?help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuthorizationSignUpRequired":

        flags = Int.read(b)

        terms_of_service = TLObject.read(b) if flags & (1 << 0) else None

        return AuthorizationSignUpRequired(terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.terms_of_service is not None else 0
        b.write(Int(flags))

        if self.terms_of_service is not None:
            b.write(self.terms_of_service.write())

        return b.getvalue()
