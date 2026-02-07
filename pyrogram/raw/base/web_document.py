# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebDocument = Union["raw.types.WebDocument", "raw.types.WebDocumentNoProxy"]


class WebDocument:  # type: ignore
    """Remote document

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebDocument
            WebDocumentNoProxy
    """

    QUALNAME = "pyrogram.raw.base.WebDocument"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
