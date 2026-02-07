# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatPhoto = Union["raw.types.ChatPhoto", "raw.types.ChatPhotoEmpty"]


class ChatPhoto:  # type: ignore
    """Object defines a group profile photo.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatPhoto
            ChatPhotoEmpty
    """

    QUALNAME = "pyrogram.raw.base.ChatPhoto"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
