# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

FileHash = Union["raw.types.FileHash"]


class FileHash:  # type: ignore
    """Hash of an uploaded file, to be checked for validity after download

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            FileHash

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.ReuploadCdnFile
            upload.GetCdnFileHashes
            upload.GetFileHashes
    """

    QUALNAME = "pyrogram.raw.base.FileHash"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
