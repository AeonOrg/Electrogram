# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EncryptedFile = Union["raw.types.EncryptedFile", "raw.types.EncryptedFileEmpty"]


class EncryptedFile:  # type: ignore
    """Seta an encrypted file.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EncryptedFile
            EncryptedFileEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadEncryptedFile
    """

    QUALNAME = "pyrogram.raw.base.EncryptedFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
