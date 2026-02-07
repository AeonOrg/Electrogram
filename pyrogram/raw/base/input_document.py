# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputDocument = Union["raw.types.InputDocument", "raw.types.InputDocumentEmpty"]


class InputDocument:  # type: ignore
    """Defines a document for subsequent interaction.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDocument
            InputDocumentEmpty
    """

    QUALNAME = "pyrogram.raw.base.InputDocument"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
