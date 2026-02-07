# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecurePasswordKdfAlgo = Union["raw.types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000", "raw.types.SecurePasswordKdfAlgoSHA512", "raw.types.SecurePasswordKdfAlgoUnknown"]


class SecurePasswordKdfAlgo:  # type: ignore
    """KDF algorithm to use for computing telegram passport hash

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000
            SecurePasswordKdfAlgoSHA512
            SecurePasswordKdfAlgoUnknown
    """

    QUALNAME = "pyrogram.raw.base.SecurePasswordKdfAlgo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
