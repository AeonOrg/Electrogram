# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BadMsgNotification = Union["raw.types.BadMsgNotification", "raw.types.BadServerSalt"]


class BadMsgNotification:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BadMsgNotification
            BadServerSalt
    """

    QUALNAME = "pyrogram.raw.base.BadMsgNotification"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
