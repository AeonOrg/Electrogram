# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmailVerifyPurpose = Union["raw.types.EmailVerifyPurposeLoginChange", "raw.types.EmailVerifyPurposeLoginSetup", "raw.types.EmailVerifyPurposePassport"]


class EmailVerifyPurpose:  # type: ignore
    """Email verification purpose

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmailVerifyPurposeLoginChange
            EmailVerifyPurposeLoginSetup
            EmailVerifyPurposePassport
    """

    QUALNAME = "pyrogram.raw.base.EmailVerifyPurpose"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
