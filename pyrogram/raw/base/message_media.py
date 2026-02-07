# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageMedia = Union["raw.types.MessageMediaContact", "raw.types.MessageMediaDice", "raw.types.MessageMediaDocument", "raw.types.MessageMediaEmpty", "raw.types.MessageMediaGame", "raw.types.MessageMediaGeo", "raw.types.MessageMediaGeoLive", "raw.types.MessageMediaGiveaway", "raw.types.MessageMediaGiveawayResults", "raw.types.MessageMediaInvoice", "raw.types.MessageMediaPaidMedia", "raw.types.MessageMediaPhoto", "raw.types.MessageMediaPoll", "raw.types.MessageMediaStory", "raw.types.MessageMediaToDo", "raw.types.MessageMediaUnsupported", "raw.types.MessageMediaVenue", "raw.types.MessageMediaVideoStream", "raw.types.MessageMediaWebPage"]


class MessageMedia:  # type: ignore
    """Media

    Constructors:
        This base type has 19 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageMediaContact
            MessageMediaDice
            MessageMediaDocument
            MessageMediaEmpty
            MessageMediaGame
            MessageMediaGeo
            MessageMediaGeoLive
            MessageMediaGiveaway
            MessageMediaGiveawayResults
            MessageMediaInvoice
            MessageMediaPaidMedia
            MessageMediaPhoto
            MessageMediaPoll
            MessageMediaStory
            MessageMediaToDo
            MessageMediaUnsupported
            MessageMediaVenue
            MessageMediaVideoStream
            MessageMediaWebPage

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    QUALNAME = "pyrogram.raw.base.MessageMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
