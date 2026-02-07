# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputUser = Union["raw.types.InputUser", "raw.types.InputUserEmpty", "raw.types.InputUserFromMessage", "raw.types.InputUserSelf"]


class InputUser:  # type: ignore
    """Defines a user for subsequent interaction.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputUser
            InputUserEmpty
            InputUserFromMessage
            InputUserSelf
    """

    QUALNAME = "pyrogram.raw.base.InputUser"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
