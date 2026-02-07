# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarsStatus = Union["raw.types.payments.StarsStatus"]


class StarsStatus:  # type: ignore
    """

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.StarsStatus

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsStatus
            payments.GetStarsTransactions
            payments.GetStarsTransactionsByID
            payments.GetStarsSubscriptions
    """

    QUALNAME = "pyrogram.raw.base.payments.StarsStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
