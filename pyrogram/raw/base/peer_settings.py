# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerSettings = Union["raw.types.PeerSettings"]


class PeerSettings:  # type: ignore
    """List of actions that are possible when interacting with this user, to be shown as suggested actions in the chat bar

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PeerSettings
    """

    QUALNAME = "pyrogram.raw.base.PeerSettings"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
