# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TermsOfServiceUpdate = Union["raw.types.help.TermsOfServiceUpdate", "raw.types.help.TermsOfServiceUpdateEmpty"]


class TermsOfServiceUpdate:  # type: ignore
    """Update of Telegram's terms of service

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.TermsOfServiceUpdate
            help.TermsOfServiceUpdateEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    QUALNAME = "pyrogram.raw.base.help.TermsOfServiceUpdate"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
