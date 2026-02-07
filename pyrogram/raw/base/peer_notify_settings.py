# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerNotifySettings = Union["raw.types.PeerNotifySettings"]


class PeerNotifySettings:  # type: ignore
    """Notification settings.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PeerNotifySettings

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetNotifySettings
    """

    QUALNAME = "pyrogram.raw.base.PeerNotifySettings"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
