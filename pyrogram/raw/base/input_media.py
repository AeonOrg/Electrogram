# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputMedia = Union["raw.types.InputMediaContact", "raw.types.InputMediaDice", "raw.types.InputMediaDocument", "raw.types.InputMediaDocumentExternal", "raw.types.InputMediaEmpty", "raw.types.InputMediaGame", "raw.types.InputMediaGeoLive", "raw.types.InputMediaGeoPoint", "raw.types.InputMediaInvoice", "raw.types.InputMediaPaidMedia", "raw.types.InputMediaPhoto", "raw.types.InputMediaPhotoExternal", "raw.types.InputMediaPoll", "raw.types.InputMediaStakeDice", "raw.types.InputMediaStory", "raw.types.InputMediaTodo", "raw.types.InputMediaUploadedDocument", "raw.types.InputMediaUploadedPhoto", "raw.types.InputMediaVenue", "raw.types.InputMediaWebPage"]


class InputMedia:  # type: ignore
    """Defines media content of a message.

    Constructors:
        This base type has 20 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMediaContact
            InputMediaDice
            InputMediaDocument
            InputMediaDocumentExternal
            InputMediaEmpty
            InputMediaGame
            InputMediaGeoLive
            InputMediaGeoPoint
            InputMediaInvoice
            InputMediaPaidMedia
            InputMediaPhoto
            InputMediaPhotoExternal
            InputMediaPoll
            InputMediaStakeDice
            InputMediaStory
            InputMediaTodo
            InputMediaUploadedDocument
            InputMediaUploadedPhoto
            InputMediaVenue
            InputMediaWebPage
    """

    QUALNAME = "pyrogram.raw.base.InputMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
