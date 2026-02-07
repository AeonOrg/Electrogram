# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

FileType = Union["raw.types.storage.FileGif", "raw.types.storage.FileJpeg", "raw.types.storage.FileMov", "raw.types.storage.FileMp3", "raw.types.storage.FileMp4", "raw.types.storage.FilePartial", "raw.types.storage.FilePdf", "raw.types.storage.FilePng", "raw.types.storage.FileUnknown", "raw.types.storage.FileWebp"]


class FileType:  # type: ignore
    """Object describes the file type.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            storage.FileGif
            storage.FileJpeg
            storage.FileMov
            storage.FileMp3
            storage.FileMp4
            storage.FilePartial
            storage.FilePdf
            storage.FilePng
            storage.FileUnknown
            storage.FileWebp
    """

    QUALNAME = "pyrogram.raw.base.storage.FileType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
