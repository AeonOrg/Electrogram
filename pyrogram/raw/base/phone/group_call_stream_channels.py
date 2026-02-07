# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GroupCallStreamChannels = Union["raw.types.phone.GroupCallStreamChannels"]


class GroupCallStreamChannels:  # type: ignore
    """Info about RTMP streams in a group call or livestream

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            phone.GroupCallStreamChannels

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStreamChannels
    """

    QUALNAME = "pyrogram.raw.base.phone.GroupCallStreamChannels"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
