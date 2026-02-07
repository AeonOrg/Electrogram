# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPrivacyKey = Union["raw.types.InputPrivacyKeyAbout", "raw.types.InputPrivacyKeyAddedByPhone", "raw.types.InputPrivacyKeyBirthday", "raw.types.InputPrivacyKeyChatInvite", "raw.types.InputPrivacyKeyForwards", "raw.types.InputPrivacyKeyNoPaidMessages", "raw.types.InputPrivacyKeyPhoneCall", "raw.types.InputPrivacyKeyPhoneNumber", "raw.types.InputPrivacyKeyPhoneP2P", "raw.types.InputPrivacyKeyProfilePhoto", "raw.types.InputPrivacyKeySavedMusic", "raw.types.InputPrivacyKeyStarGiftsAutoSave", "raw.types.InputPrivacyKeyStatusTimestamp", "raw.types.InputPrivacyKeyVoiceMessages"]


class InputPrivacyKey:  # type: ignore
    """Privacy keys together with privacy rules » indicate what can or can't someone do and are specified by a PrivacyKey constructor, and its input counterpart InputPrivacyKey.

    Constructors:
        This base type has 14 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPrivacyKeyAbout
            InputPrivacyKeyAddedByPhone
            InputPrivacyKeyBirthday
            InputPrivacyKeyChatInvite
            InputPrivacyKeyForwards
            InputPrivacyKeyNoPaidMessages
            InputPrivacyKeyPhoneCall
            InputPrivacyKeyPhoneNumber
            InputPrivacyKeyPhoneP2P
            InputPrivacyKeyProfilePhoto
            InputPrivacyKeySavedMusic
            InputPrivacyKeyStarGiftsAutoSave
            InputPrivacyKeyStatusTimestamp
            InputPrivacyKeyVoiceMessages
    """

    QUALNAME = "pyrogram.raw.base.InputPrivacyKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
