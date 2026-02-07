# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DialogFilterSuggested = Union["raw.types.DialogFilterSuggested"]


class DialogFilterSuggested:  # type: ignore
    """Suggested dialog filters (folder »)

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DialogFilterSuggested

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSuggestedDialogFilters
    """

    QUALNAME = "pyrogram.raw.base.DialogFilterSuggested"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
