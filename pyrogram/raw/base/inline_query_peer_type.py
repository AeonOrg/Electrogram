# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InlineQueryPeerType = Union["raw.types.InlineQueryPeerTypeBotPM", "raw.types.InlineQueryPeerTypeBroadcast", "raw.types.InlineQueryPeerTypeChat", "raw.types.InlineQueryPeerTypeMegagroup", "raw.types.InlineQueryPeerTypePM", "raw.types.InlineQueryPeerTypeSameBotPM"]


class InlineQueryPeerType:  # type: ignore
    """Inline query peer type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InlineQueryPeerTypeBotPM
            InlineQueryPeerTypeBroadcast
            InlineQueryPeerTypeChat
            InlineQueryPeerTypeMegagroup
            InlineQueryPeerTypePM
            InlineQueryPeerTypeSameBotPM
    """

    QUALNAME = "pyrogram.raw.base.InlineQueryPeerType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
