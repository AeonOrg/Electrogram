# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SendAsPeers = Union["raw.types.channels.SendAsPeers"]


class SendAsPeers:  # type: ignore
    """A list of peers that can be used to send messages in a specific group

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            channels.SendAsPeers

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetSendAs
    """

    QUALNAME = "pyrogram.raw.base.channels.SendAsPeers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
