# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputCheckPasswordSRP = Union["raw.types.InputCheckPasswordEmpty", "raw.types.InputCheckPasswordSRP"]


class InputCheckPasswordSRP:  # type: ignore
    """Constructors for checking the validity of a 2FA SRP password

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputCheckPasswordEmpty
            InputCheckPasswordSRP
    """

    QUALNAME = "pyrogram.raw.base.InputCheckPasswordSRP"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
