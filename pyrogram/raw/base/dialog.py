# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Dialog = Union["raw.types.Dialog", "raw.types.DialogFolder"]


class Dialog:  # type: ignore
    """Chat info.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            Dialog
            DialogFolder
    """

    QUALNAME = "pyrogram.raw.base.Dialog"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
