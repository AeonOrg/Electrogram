# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EligibilityToJoin = Union["raw.types.smsjobs.EligibleToJoin"]


class EligibilityToJoin:  # type: ignore
    """

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            smsjobs.EligibleToJoin

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.IsEligibleToJoin
    """

    QUALNAME = "pyrogram.raw.base.smsjobs.EligibilityToJoin"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
