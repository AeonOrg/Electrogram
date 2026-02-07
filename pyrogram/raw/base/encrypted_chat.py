# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EncryptedChat = Union["raw.types.EncryptedChat", "raw.types.EncryptedChatDiscarded", "raw.types.EncryptedChatEmpty", "raw.types.EncryptedChatRequested", "raw.types.EncryptedChatWaiting"]


class EncryptedChat:  # type: ignore
    """Object contains info on an encrypted chat.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EncryptedChat
            EncryptedChatDiscarded
            EncryptedChatEmpty
            EncryptedChatRequested
            EncryptedChatWaiting

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    QUALNAME = "pyrogram.raw.base.EncryptedChat"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
