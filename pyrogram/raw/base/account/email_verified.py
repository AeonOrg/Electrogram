# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmailVerified = Union["raw.types.account.EmailVerified", "raw.types.account.EmailVerifiedLogin"]


class EmailVerified:  # type: ignore
    """Email verification status

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.EmailVerified
            account.EmailVerifiedLogin

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.VerifyEmail
    """

    QUALNAME = "pyrogram.raw.base.account.EmailVerified"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
