# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CdnPublicKey = Union["raw.types.CdnPublicKey"]


class CdnPublicKey:  # type: ignore
    """Public key to use only during handshakes to CDN DCs.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            CdnPublicKey
    """

    QUALNAME = "pyrogram.raw.base.CdnPublicKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
