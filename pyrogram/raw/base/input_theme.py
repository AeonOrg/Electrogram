# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputTheme = Union["raw.types.InputTheme", "raw.types.InputThemeSlug"]


class InputTheme:  # type: ignore
    """Cloud theme

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputTheme
            InputThemeSlug
    """

    QUALNAME = "pyrogram.raw.base.InputTheme"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
