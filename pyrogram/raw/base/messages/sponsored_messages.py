# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SponsoredMessages = Union["raw.types.messages.SponsoredMessages", "raw.types.messages.SponsoredMessagesEmpty"]


class SponsoredMessages:  # type: ignore
    """A set of sponsored messages associated with a channel

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SponsoredMessages
            messages.SponsoredMessagesEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSponsoredMessages
    """

    QUALNAME = "pyrogram.raw.base.messages.SponsoredMessages"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
