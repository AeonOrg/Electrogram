# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebFile = Union["raw.types.upload.WebFile"]


class WebFile:  # type: ignore
    """Remote file

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            upload.WebFile

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetWebFile
    """

    QUALNAME = "pyrogram.raw.base.upload.WebFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
