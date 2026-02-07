# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureFile = Union["raw.types.SecureFile", "raw.types.SecureFileEmpty"]


class SecureFile:  # type: ignore
    """Secure passport file, for more info see the passport docs »

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureFile
            SecureFileEmpty
    """

    QUALNAME = "pyrogram.raw.base.SecureFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
