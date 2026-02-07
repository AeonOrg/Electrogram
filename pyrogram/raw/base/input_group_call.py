# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputGroupCall = Union["raw.types.InputGroupCall", "raw.types.InputGroupCallInviteMessage", "raw.types.InputGroupCallSlug"]


class InputGroupCall:  # type: ignore
    """Indicates a group call

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputGroupCall
            InputGroupCallInviteMessage
            InputGroupCallSlug
    """

    QUALNAME = "pyrogram.raw.base.InputGroupCall"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
