# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Authorizations = Union["raw.types.account.Authorizations"]


class Authorizations:  # type: ignore
    """Logged-in sessions

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.Authorizations

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAuthorizations
    """

    QUALNAME = "pyrogram.raw.base.account.Authorizations"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
