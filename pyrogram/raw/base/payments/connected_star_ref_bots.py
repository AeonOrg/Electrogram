# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ConnectedStarRefBots = Union["raw.types.payments.ConnectedStarRefBots"]


class ConnectedStarRefBots:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.ConnectedStarRefBots

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetConnectedStarRefBots
            payments.GetConnectedStarRefBot
            payments.ConnectStarRefBot
            payments.EditConnectedStarRefBot
    """

    QUALNAME = "pyrogram.raw.base.payments.ConnectedStarRefBots"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
