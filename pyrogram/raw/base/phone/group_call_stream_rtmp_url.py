# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GroupCallStreamRtmpUrl = Union["raw.types.phone.GroupCallStreamRtmpUrl"]


class GroupCallStreamRtmpUrl:  # type: ignore
    """RTMP URL and stream key to be used in streaming software

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            phone.GroupCallStreamRtmpUrl

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStreamRtmpUrl
    """

    QUALNAME = "pyrogram.raw.base.phone.GroupCallStreamRtmpUrl"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
