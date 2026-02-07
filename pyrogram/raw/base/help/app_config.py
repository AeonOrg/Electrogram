# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AppConfig = Union["raw.types.help.AppConfig", "raw.types.help.AppConfigNotModified"]


class AppConfig:  # type: ignore
    """Contains various client configuration parameters

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.AppConfig
            help.AppConfigNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    QUALNAME = "pyrogram.raw.base.help.AppConfig"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
