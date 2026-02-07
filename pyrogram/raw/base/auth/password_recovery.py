# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PasswordRecovery = Union["raw.types.auth.PasswordRecovery"]


class PasswordRecovery:  # type: ignore
    """Recovery info of a 2FA password, only for accounts with a recovery email configured.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.PasswordRecovery

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.RequestPasswordRecovery
    """

    QUALNAME = "pyrogram.raw.base.auth.PasswordRecovery"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
