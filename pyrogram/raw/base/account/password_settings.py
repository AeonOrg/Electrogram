# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PasswordSettings = Union["raw.types.account.PasswordSettings"]


class PasswordSettings:  # type: ignore
    """Private info associated to the password info (recovery email, telegram passport info & so on)

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.PasswordSettings

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPasswordSettings
    """

    QUALNAME = "pyrogram.raw.base.account.PasswordSettings"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
