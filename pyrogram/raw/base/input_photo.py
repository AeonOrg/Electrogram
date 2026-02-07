# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPhoto = Union["raw.types.InputPhoto", "raw.types.InputPhotoEmpty"]


class InputPhoto:  # type: ignore
    """Defines a photo for further interaction.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPhoto
            InputPhotoEmpty
    """

    QUALNAME = "pyrogram.raw.base.InputPhoto"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
