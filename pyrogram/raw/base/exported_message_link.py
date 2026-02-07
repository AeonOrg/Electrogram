# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedMessageLink = Union["raw.types.ExportedMessageLink"]


class ExportedMessageLink:  # type: ignore
    """HTTP link and embed info of channel message

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ExportedMessageLink

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.ExportMessageLink
    """

    QUALNAME = "pyrogram.raw.base.ExportedMessageLink"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
