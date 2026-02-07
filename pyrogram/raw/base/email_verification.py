# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmailVerification = Union["raw.types.EmailVerificationApple", "raw.types.EmailVerificationCode", "raw.types.EmailVerificationGoogle"]


class EmailVerification:  # type: ignore
    """Email verification code or token

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmailVerificationApple
            EmailVerificationCode
            EmailVerificationGoogle
    """

    QUALNAME = "pyrogram.raw.base.EmailVerification"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
