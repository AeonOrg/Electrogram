# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputWebFileLocation = Union["raw.types.InputWebFileAudioAlbumThumbLocation", "raw.types.InputWebFileGeoPointLocation", "raw.types.InputWebFileLocation"]


class InputWebFileLocation:  # type: ignore
    """Location of remote file

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputWebFileAudioAlbumThumbLocation
            InputWebFileGeoPointLocation
            InputWebFileLocation
    """

    QUALNAME = "pyrogram.raw.base.InputWebFileLocation"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
