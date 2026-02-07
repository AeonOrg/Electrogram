# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GlobalPrivacySettings = Union["raw.types.GlobalPrivacySettings"]


class GlobalPrivacySettings:  # type: ignore
    """Global privacy settings

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            GlobalPrivacySettings

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetGlobalPrivacySettings
            account.SetGlobalPrivacySettings
    """

    QUALNAME = "pyrogram.raw.base.GlobalPrivacySettings"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
