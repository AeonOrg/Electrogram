# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebViewMessageSent = Union["raw.types.WebViewMessageSent"]


class WebViewMessageSent:  # type: ignore
    """Contains information about an inline message sent by a Web App on behalf of a user.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebViewMessageSent

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SendWebViewResultMessage
    """

    QUALNAME = "pyrogram.raw.base.WebViewMessageSent"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
