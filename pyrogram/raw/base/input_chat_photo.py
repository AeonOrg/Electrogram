# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputChatPhoto = Union["raw.types.InputChatPhoto", "raw.types.InputChatPhotoEmpty", "raw.types.InputChatUploadedPhoto"]


class InputChatPhoto:  # type: ignore
    """Defines a new group profile photo.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChatPhoto
            InputChatPhotoEmpty
            InputChatUploadedPhoto
    """

    QUALNAME = "pyrogram.raw.base.InputChatPhoto"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
