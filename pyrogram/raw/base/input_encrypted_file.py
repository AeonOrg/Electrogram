# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputEncryptedFile = Union["raw.types.InputEncryptedFile", "raw.types.InputEncryptedFileBigUploaded", "raw.types.InputEncryptedFileEmpty", "raw.types.InputEncryptedFileUploaded"]


class InputEncryptedFile:  # type: ignore
    """Object sets encrypted file for attachment

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputEncryptedFile
            InputEncryptedFileBigUploaded
            InputEncryptedFileEmpty
            InputEncryptedFileUploaded
    """

    QUALNAME = "pyrogram.raw.base.InputEncryptedFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
