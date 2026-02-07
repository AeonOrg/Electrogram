# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DialogPeer = Union["raw.types.DialogPeer", "raw.types.DialogPeerFolder"]


class DialogPeer:  # type: ignore
    """Peer, or all peers in a folder

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DialogPeer
            DialogPeerFolder

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogUnreadMarks
    """

    QUALNAME = "pyrogram.raw.base.DialogPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
