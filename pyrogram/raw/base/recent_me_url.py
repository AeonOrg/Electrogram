# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RecentMeUrl = Union["raw.types.RecentMeUrlChat", "raw.types.RecentMeUrlChatInvite", "raw.types.RecentMeUrlStickerSet", "raw.types.RecentMeUrlUnknown", "raw.types.RecentMeUrlUser"]


class RecentMeUrl:  # type: ignore
    """Recent t.me urls

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RecentMeUrlChat
            RecentMeUrlChatInvite
            RecentMeUrlStickerSet
            RecentMeUrlUnknown
            RecentMeUrlUser
    """

    QUALNAME = "pyrogram.raw.base.RecentMeUrl"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
