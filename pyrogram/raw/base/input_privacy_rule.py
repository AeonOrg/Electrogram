# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPrivacyRule = Union["raw.types.InputPrivacyValueAllowAll", "raw.types.InputPrivacyValueAllowBots", "raw.types.InputPrivacyValueAllowChatParticipants", "raw.types.InputPrivacyValueAllowCloseFriends", "raw.types.InputPrivacyValueAllowContacts", "raw.types.InputPrivacyValueAllowPremium", "raw.types.InputPrivacyValueAllowUsers", "raw.types.InputPrivacyValueDisallowAll", "raw.types.InputPrivacyValueDisallowBots", "raw.types.InputPrivacyValueDisallowChatParticipants", "raw.types.InputPrivacyValueDisallowContacts", "raw.types.InputPrivacyValueDisallowUsers"]


class InputPrivacyRule:  # type: ignore
    """Privacy rules indicate who can or can't do something and are specified by a PrivacyRule, and its input counterpart InputPrivacyRule.

    Constructors:
        This base type has 12 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPrivacyValueAllowAll
            InputPrivacyValueAllowBots
            InputPrivacyValueAllowChatParticipants
            InputPrivacyValueAllowCloseFriends
            InputPrivacyValueAllowContacts
            InputPrivacyValueAllowPremium
            InputPrivacyValueAllowUsers
            InputPrivacyValueDisallowAll
            InputPrivacyValueDisallowBots
            InputPrivacyValueDisallowChatParticipants
            InputPrivacyValueDisallowContacts
            InputPrivacyValueDisallowUsers
    """

    QUALNAME = "pyrogram.raw.base.InputPrivacyRule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
