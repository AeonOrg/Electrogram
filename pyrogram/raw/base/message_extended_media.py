# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageExtendedMedia = Union["raw.types.MessageExtendedMedia", "raw.types.MessageExtendedMediaPreview"]


class MessageExtendedMedia:  # type: ignore
    """Extended media

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageExtendedMedia
            MessageExtendedMediaPreview
    """

    QUALNAME = "pyrogram.raw.base.MessageExtendedMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
