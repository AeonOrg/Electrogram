# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputFile = Union["raw.types.InputFile", "raw.types.InputFileBig", "raw.types.InputFileStoryDocument"]


class InputFile:  # type: ignore
    """Defines a file uploaded by the client.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputFile
            InputFileBig
            InputFileStoryDocument
    """

    QUALNAME = "pyrogram.raw.base.InputFile"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
