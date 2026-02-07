# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Themes = Union["raw.types.account.Themes", "raw.types.account.ThemesNotModified"]


class Themes:  # type: ignore
    """Installed themes

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.Themes
            account.ThemesNotModified

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetThemes
            account.GetChatThemes
    """

    QUALNAME = "pyrogram.raw.base.account.Themes"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
