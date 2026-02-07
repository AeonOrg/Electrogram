# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PrivacyKey = Union["raw.types.PrivacyKeyAbout", "raw.types.PrivacyKeyAddedByPhone", "raw.types.PrivacyKeyBirthday", "raw.types.PrivacyKeyChatInvite", "raw.types.PrivacyKeyForwards", "raw.types.PrivacyKeyNoPaidMessages", "raw.types.PrivacyKeyPhoneCall", "raw.types.PrivacyKeyPhoneNumber", "raw.types.PrivacyKeyPhoneP2P", "raw.types.PrivacyKeyProfilePhoto", "raw.types.PrivacyKeySavedMusic", "raw.types.PrivacyKeyStarGiftsAutoSave", "raw.types.PrivacyKeyStatusTimestamp", "raw.types.PrivacyKeyVoiceMessages"]


class PrivacyKey:  # type: ignore
    """Privacy keys together with privacy rules » indicate what can or can't someone do and are specified by a PrivacyKey constructor, and its input counterpart InputPrivacyKey.

    Constructors:
        This base type has 14 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrivacyKeyAbout
            PrivacyKeyAddedByPhone
            PrivacyKeyBirthday
            PrivacyKeyChatInvite
            PrivacyKeyForwards
            PrivacyKeyNoPaidMessages
            PrivacyKeyPhoneCall
            PrivacyKeyPhoneNumber
            PrivacyKeyPhoneP2P
            PrivacyKeyProfilePhoto
            PrivacyKeySavedMusic
            PrivacyKeyStarGiftsAutoSave
            PrivacyKeyStatusTimestamp
            PrivacyKeyVoiceMessages
    """

    QUALNAME = "pyrogram.raw.base.PrivacyKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
