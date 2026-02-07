# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ReactionNotificationsFrom = Union["raw.types.ReactionNotificationsFromAll", "raw.types.ReactionNotificationsFromContacts"]


class ReactionNotificationsFrom:  # type: ignore
    """

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ReactionNotificationsFromAll
            ReactionNotificationsFromContacts
    """

    QUALNAME = "pyrogram.raw.base.ReactionNotificationsFrom"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
