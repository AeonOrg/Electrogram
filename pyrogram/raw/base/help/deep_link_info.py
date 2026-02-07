# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DeepLinkInfo = Union["raw.types.help.DeepLinkInfo", "raw.types.help.DeepLinkInfoEmpty"]


class DeepLinkInfo:  # type: ignore
    """Contains information about an unsupported deep link »

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.DeepLinkInfo
            help.DeepLinkInfoEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetDeepLinkInfo
    """

    QUALNAME = "pyrogram.raw.base.help.DeepLinkInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
