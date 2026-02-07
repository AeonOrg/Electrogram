# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotApp = Union["raw.types.BotApp", "raw.types.BotAppNotModified"]


class BotApp:  # type: ignore
    """Contains information about a direct link Mini App.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotApp
            BotAppNotModified
    """

    QUALNAME = "pyrogram.raw.base.BotApp"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
