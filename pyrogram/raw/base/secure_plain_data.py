# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecurePlainData = Union["raw.types.SecurePlainEmail", "raw.types.SecurePlainPhone"]


class SecurePlainData:  # type: ignore
    """Plaintext verified passport data.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecurePlainEmail
            SecurePlainPhone
    """

    QUALNAME = "pyrogram.raw.base.SecurePlainData"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
