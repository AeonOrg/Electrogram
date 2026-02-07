# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerStories = Union["raw.types.stories.PeerStories"]


class PeerStories:  # type: ignore
    """Active story list of a specific peer.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.PeerStories

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetPeerStories
    """

    QUALNAME = "pyrogram.raw.base.stories.PeerStories"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
