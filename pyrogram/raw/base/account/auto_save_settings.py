# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AutoSaveSettings = Union["raw.types.account.AutoSaveSettings"]


class AutoSaveSettings:  # type: ignore
    """Contains media autosave settings

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.AutoSaveSettings

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAutoSaveSettings
    """

    QUALNAME = "pyrogram.raw.base.account.AutoSaveSettings"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
