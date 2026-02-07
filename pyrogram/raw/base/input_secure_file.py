# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputSecureFile = Union["raw.types.InputSecureFile", "raw.types.InputSecureFileUploaded"]


class InputSecureFile:  # type: ignore
    """Secure passport file, for more info see the passport docs »

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputSecureFile
            InputSecureFileUploaded
    """

    QUALNAME = "pyrogram.raw.base.InputSecureFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
