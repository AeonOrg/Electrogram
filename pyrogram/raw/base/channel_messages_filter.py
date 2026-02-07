# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelMessagesFilter = Union["raw.types.ChannelMessagesFilter", "raw.types.ChannelMessagesFilterEmpty"]


class ChannelMessagesFilter:  # type: ignore
    """Filter for fetching only certain types of channel messages

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelMessagesFilter
            ChannelMessagesFilterEmpty
    """

    QUALNAME = "pyrogram.raw.base.ChannelMessagesFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
