# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPeer = Union["raw.types.InputPeerChannel", "raw.types.InputPeerChannelFromMessage", "raw.types.InputPeerChat", "raw.types.InputPeerEmpty", "raw.types.InputPeerSelf", "raw.types.InputPeerUser", "raw.types.InputPeerUserFromMessage"]


class InputPeer:  # type: ignore
    """Peer

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPeerChannel
            InputPeerChannelFromMessage
            InputPeerChat
            InputPeerEmpty
            InputPeerSelf
            InputPeerUser
            InputPeerUserFromMessage
    """

    QUALNAME = "pyrogram.raw.base.InputPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
