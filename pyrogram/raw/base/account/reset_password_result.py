# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ResetPasswordResult = Union["raw.types.account.ResetPasswordFailedWait", "raw.types.account.ResetPasswordOk", "raw.types.account.ResetPasswordRequestedWait"]


class ResetPasswordResult:  # type: ignore
    """Result of an account.resetPassword request.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.ResetPasswordFailedWait
            account.ResetPasswordOk
            account.ResetPasswordRequestedWait

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    QUALNAME = "pyrogram.raw.base.account.ResetPasswordResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
