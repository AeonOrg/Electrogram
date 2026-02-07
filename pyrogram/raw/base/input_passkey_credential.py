# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPasskeyCredential = Union["raw.types.InputPasskeyCredentialFirebasePNV", "raw.types.InputPasskeyCredentialPublicKey"]


class InputPasskeyCredential:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPasskeyCredentialFirebasePNV
            InputPasskeyCredentialPublicKey
    """

    QUALNAME = "pyrogram.raw.base.InputPasskeyCredential"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
