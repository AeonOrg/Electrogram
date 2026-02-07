# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputFileLocation = Union["raw.types.InputDocumentFileLocation", "raw.types.InputEncryptedFileLocation", "raw.types.InputFileLocation", "raw.types.InputGroupCallStream", "raw.types.InputPeerPhotoFileLocation", "raw.types.InputPhotoFileLocation", "raw.types.InputPhotoLegacyFileLocation", "raw.types.InputSecureFileLocation", "raw.types.InputStickerSetThumb", "raw.types.InputTakeoutFileLocation"]


class InputFileLocation:  # type: ignore
    """Defines the location of a file for download.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputDocumentFileLocation
            InputEncryptedFileLocation
            InputFileLocation
            InputGroupCallStream
            InputPeerPhotoFileLocation
            InputPhotoFileLocation
            InputPhotoLegacyFileLocation
            InputSecureFileLocation
            InputStickerSetThumb
            InputTakeoutFileLocation
    """

    QUALNAME = "pyrogram.raw.base.InputFileLocation"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
