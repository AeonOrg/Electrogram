# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebAuthorizations = Union["raw.types.account.WebAuthorizations"]


class WebAuthorizations:  # type: ignore
    """Web authorizations

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.WebAuthorizations

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebAuthorizations
    """

    QUALNAME = "pyrogram.raw.base.account.WebAuthorizations"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
