# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ValidatedRequestedInfo = Union["raw.types.payments.ValidatedRequestedInfo"]


class ValidatedRequestedInfo:  # type: ignore
    """Validated requested info

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.ValidatedRequestedInfo

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.ValidateRequestedInfo
    """

    QUALNAME = "pyrogram.raw.base.payments.ValidatedRequestedInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
