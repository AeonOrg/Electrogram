# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EncryptedMessage = Union["raw.types.EncryptedMessage", "raw.types.EncryptedMessageService"]


class EncryptedMessage:  # type: ignore
    """Object contains encrypted message.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EncryptedMessage
            EncryptedMessageService
    """

    QUALNAME = "pyrogram.raw.base.EncryptedMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
