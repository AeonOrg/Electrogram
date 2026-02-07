# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputBotApp = Union["raw.types.InputBotAppID", "raw.types.InputBotAppShortName"]


class InputBotApp:  # type: ignore
    """Used to fetch information about a direct link Mini App

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputBotAppID
            InputBotAppShortName
    """

    QUALNAME = "pyrogram.raw.base.InputBotApp"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
