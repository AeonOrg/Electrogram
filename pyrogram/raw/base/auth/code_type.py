# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CodeType = Union["raw.types.auth.CodeTypeCall", "raw.types.auth.CodeTypeFlashCall", "raw.types.auth.CodeTypeFragmentSms", "raw.types.auth.CodeTypeMissedCall", "raw.types.auth.CodeTypeSms"]


class CodeType:  # type: ignore
    """Type of verification code that will be sent next if you call the resendCode method

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.CodeTypeCall
            auth.CodeTypeFlashCall
            auth.CodeTypeFragmentSms
            auth.CodeTypeMissedCall
            auth.CodeTypeSms
    """

    QUALNAME = "pyrogram.raw.base.auth.CodeType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
