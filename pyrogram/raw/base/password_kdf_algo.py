# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PasswordKdfAlgo = Union["raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", "raw.types.PasswordKdfAlgoUnknown"]


class PasswordKdfAlgo:  # type: ignore
    """Key derivation function to use when generating the password hash for SRP two-factor authorization

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
            PasswordKdfAlgoUnknown
    """

    QUALNAME = "pyrogram.raw.base.PasswordKdfAlgo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
