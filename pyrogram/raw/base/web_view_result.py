# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebViewResult = Union["raw.types.WebViewResultUrl"]


class WebViewResult:  # type: ignore
    """Contains the webview URL with appropriate theme and user info parameters added

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebViewResultUrl

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestWebView
            messages.RequestSimpleWebView
            messages.RequestAppWebView
            messages.RequestMainWebView
    """

    QUALNAME = "pyrogram.raw.base.WebViewResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
