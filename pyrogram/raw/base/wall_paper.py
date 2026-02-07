# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WallPaper = Union["raw.types.WallPaper", "raw.types.WallPaperNoFile"]


class WallPaper:  # type: ignore
    """Object contains info on a wallpaper.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WallPaper
            WallPaperNoFile

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWallPaper
            account.UploadWallPaper
            account.GetMultiWallPapers
    """

    QUALNAME = "pyrogram.raw.base.WallPaper"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
