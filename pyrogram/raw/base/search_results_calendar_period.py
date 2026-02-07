# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SearchResultsCalendarPeriod = Union["raw.types.SearchResultsCalendarPeriod"]


class SearchResultsCalendarPeriod:  # type: ignore
    """Information about found messages sent on a specific day, used to split the messages in messages.searchResultsCalendar constructors by days.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SearchResultsCalendarPeriod
    """

    QUALNAME = "pyrogram.raw.base.SearchResultsCalendarPeriod"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
