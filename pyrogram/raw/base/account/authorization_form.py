# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AuthorizationForm = Union["raw.types.account.AuthorizationForm"]


class AuthorizationForm:  # type: ignore
    """Authorization form

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.AuthorizationForm

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAuthorizationForm
    """

    QUALNAME = "pyrogram.raw.base.account.AuthorizationForm"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
