# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SendMessageAction = Union["raw.types.SendMessageCancelAction", "raw.types.SendMessageChooseContactAction", "raw.types.SendMessageChooseStickerAction", "raw.types.SendMessageEmojiInteraction", "raw.types.SendMessageEmojiInteractionSeen", "raw.types.SendMessageGamePlayAction", "raw.types.SendMessageGeoLocationAction", "raw.types.SendMessageHistoryImportAction", "raw.types.SendMessageRecordAudioAction", "raw.types.SendMessageRecordRoundAction", "raw.types.SendMessageRecordVideoAction", "raw.types.SendMessageTextDraftAction", "raw.types.SendMessageTypingAction", "raw.types.SendMessageUploadAudioAction", "raw.types.SendMessageUploadDocumentAction", "raw.types.SendMessageUploadPhotoAction", "raw.types.SendMessageUploadRoundAction", "raw.types.SendMessageUploadVideoAction", "raw.types.SpeakingInGroupCallAction"]


class SendMessageAction:  # type: ignore
    """User actions. Use this to provide users with detailed info about their chat partner's actions: typing or sending attachments of all kinds.

    Constructors:
        This base type has 19 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SendMessageCancelAction
            SendMessageChooseContactAction
            SendMessageChooseStickerAction
            SendMessageEmojiInteraction
            SendMessageEmojiInteractionSeen
            SendMessageGamePlayAction
            SendMessageGeoLocationAction
            SendMessageHistoryImportAction
            SendMessageRecordAudioAction
            SendMessageRecordRoundAction
            SendMessageRecordVideoAction
            SendMessageTextDraftAction
            SendMessageTypingAction
            SendMessageUploadAudioAction
            SendMessageUploadDocumentAction
            SendMessageUploadPhotoAction
            SendMessageUploadRoundAction
            SendMessageUploadVideoAction
            SpeakingInGroupCallAction
    """

    QUALNAME = "pyrogram.raw.base.SendMessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
