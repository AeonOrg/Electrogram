# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputChannel = Union["raw.types.InputChannel", "raw.types.InputChannelEmpty", "raw.types.InputChannelFromMessage"]


class InputChannel:  # type: ignore
    """Represents a channel

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChannel
            InputChannelEmpty
            InputChannelFromMessage
    """

    QUALNAME = "pyrogram.raw.base.InputChannel"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
