# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebPage = Union["raw.types.WebPage", "raw.types.WebPageEmpty", "raw.types.WebPageNotModified", "raw.types.WebPagePending", "raw.types.WebPageUrlPending"]


class WebPage:  # type: ignore
    """Instant View webpage preview

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPage
            WebPageEmpty
            WebPageNotModified
            WebPagePending
            WebPageUrlPending
    """

    QUALNAME = "pyrogram.raw.base.WebPage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
