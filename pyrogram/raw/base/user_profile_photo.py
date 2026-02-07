# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserProfilePhoto = Union["raw.types.UserProfilePhoto", "raw.types.UserProfilePhotoEmpty"]


class UserProfilePhoto:  # type: ignore
    """Object contains info on the user's profile photo.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UserProfilePhoto
            UserProfilePhotoEmpty
    """

    QUALNAME = "pyrogram.raw.base.UserProfilePhoto"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
