# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

JoinAsPeers = Union["raw.types.phone.JoinAsPeers"]


class JoinAsPeers:  # type: ignore
    """A list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            phone.JoinAsPeers

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallJoinAs
    """

    QUALNAME = "pyrogram.raw.base.phone.JoinAsPeers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
