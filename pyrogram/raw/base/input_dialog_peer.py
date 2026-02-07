# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputDialogPeer = Union["raw.types.InputDialogPeer", "raw.types.InputDialogPeerFolder"]


class InputDialogPeer:  # type: ignore
    """Peer, or all peers in a certain folder

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDialogPeer
            InputDialogPeerFolder
    """

    QUALNAME = "pyrogram.raw.base.InputDialogPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
