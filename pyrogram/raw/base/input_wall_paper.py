# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputWallPaper = Union["raw.types.InputWallPaper", "raw.types.InputWallPaperNoFile", "raw.types.InputWallPaperSlug"]


class InputWallPaper:  # type: ignore
    """Wallpaper

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputWallPaper
            InputWallPaperNoFile
            InputWallPaperSlug
    """

    QUALNAME = "pyrogram.raw.base.InputWallPaper"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
