# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputContact = Union["raw.types.InputPhoneContact"]


class InputContact:  # type: ignore
    """Object defines a contact from the user's phone book.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPhoneContact
    """

    QUALNAME = "pyrogram.raw.base.InputContact"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
