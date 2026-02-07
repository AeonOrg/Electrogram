# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Message = Union["raw.types.Message", "raw.types.MessageEmpty", "raw.types.MessageService"]


class Message:  # type: ignore
    """Object describing a message.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            Message
            MessageEmpty
            MessageService
    """

    QUALNAME = "pyrogram.raw.base.Message"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
