# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputGame = Union["raw.types.InputGameID", "raw.types.InputGameShortName"]


class InputGame:  # type: ignore
    """A game to send

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputGameID
            InputGameShortName
    """

    QUALNAME = "pyrogram.raw.base.InputGame"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
