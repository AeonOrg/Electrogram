# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputStickeredMedia = Union["raw.types.InputStickeredMediaDocument", "raw.types.InputStickeredMediaPhoto"]


class InputStickeredMedia:  # type: ignore
    """Represents a media with attached stickers

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStickeredMediaDocument
            InputStickeredMediaPhoto
    """

    QUALNAME = "pyrogram.raw.base.InputStickeredMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
