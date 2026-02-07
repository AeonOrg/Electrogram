# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TranscribedAudio = Union["raw.types.messages.TranscribedAudio"]


class TranscribedAudio:  # type: ignore
    """Transcribed text from a voice message

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.TranscribedAudio

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranscribeAudio
    """

    QUALNAME = "pyrogram.raw.base.messages.TranscribedAudio"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
