# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

NotifyPeer = Union["raw.types.NotifyBroadcasts", "raw.types.NotifyChats", "raw.types.NotifyForumTopic", "raw.types.NotifyPeer", "raw.types.NotifyUsers"]


class NotifyPeer:  # type: ignore
    """Object defines the set of users and/or groups that generate notifications.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            NotifyBroadcasts
            NotifyChats
            NotifyForumTopic
            NotifyPeer
            NotifyUsers
    """

    QUALNAME = "pyrogram.raw.base.NotifyPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
