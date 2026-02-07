# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedContactToken = Union["raw.types.ExportedContactToken"]


class ExportedContactToken:  # type: ignore
    """Describes a temporary profile link.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ExportedContactToken

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ExportContactToken
    """

    QUALNAME = "pyrogram.raw.base.ExportedContactToken"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
