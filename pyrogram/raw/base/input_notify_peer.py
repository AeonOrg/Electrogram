# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputNotifyPeer = Union["raw.types.InputNotifyBroadcasts", "raw.types.InputNotifyChats", "raw.types.InputNotifyForumTopic", "raw.types.InputNotifyPeer", "raw.types.InputNotifyUsers"]


class InputNotifyPeer:  # type: ignore
    """Object defines the set of users and/or groups that generate notifications.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputNotifyBroadcasts
            InputNotifyChats
            InputNotifyForumTopic
            InputNotifyPeer
            InputNotifyUsers
    """

    QUALNAME = "pyrogram.raw.base.InputNotifyPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
