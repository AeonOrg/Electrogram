# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SentEncryptedMessage = Union["raw.types.messages.SentEncryptedFile", "raw.types.messages.SentEncryptedMessage"]


class SentEncryptedMessage:  # type: ignore
    """Contains info on message sent to an encrypted chat.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SentEncryptedFile
            messages.SentEncryptedMessage

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SendEncrypted
            messages.SendEncryptedFile
            messages.SendEncryptedService
    """

    QUALNAME = "pyrogram.raw.base.messages.SentEncryptedMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
