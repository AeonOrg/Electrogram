# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CdnConfig = Union["raw.types.CdnConfig"]


class CdnConfig:  # type: ignore
    """Configuration for CDN file downloads.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            CdnConfig

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCdnConfig
    """

    QUALNAME = "pyrogram.raw.base.CdnConfig"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
