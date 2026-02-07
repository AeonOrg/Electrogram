# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SearchResultsCalendar = Union["raw.types.messages.SearchResultsCalendar"]


class SearchResultsCalendar:  # type: ignore
    """Information about found messages sent on a specific day

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SearchResultsCalendar

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchResultsCalendar
    """

    QUALNAME = "pyrogram.raw.base.messages.SearchResultsCalendar"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
