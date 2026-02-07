# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelLocation = Union["raw.types.ChannelLocation", "raw.types.ChannelLocationEmpty"]


class ChannelLocation:  # type: ignore
    """Geographical location of supergroup (geogroups)

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelLocation
            ChannelLocationEmpty
    """

    QUALNAME = "pyrogram.raw.base.ChannelLocation"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
