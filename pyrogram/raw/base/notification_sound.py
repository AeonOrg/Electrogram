# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

NotificationSound = Union["raw.types.NotificationSoundDefault", "raw.types.NotificationSoundLocal", "raw.types.NotificationSoundNone", "raw.types.NotificationSoundRingtone"]


class NotificationSound:  # type: ignore
    """Represents a notification sound

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            NotificationSoundDefault
            NotificationSoundLocal
            NotificationSoundNone
            NotificationSoundRingtone
    """

    QUALNAME = "pyrogram.raw.base.NotificationSound"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
