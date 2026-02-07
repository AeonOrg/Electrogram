# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaidReactionPrivacy = Union["raw.types.PaidReactionPrivacyAnonymous", "raw.types.PaidReactionPrivacyDefault", "raw.types.PaidReactionPrivacyPeer"]


class PaidReactionPrivacy:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PaidReactionPrivacyAnonymous
            PaidReactionPrivacyDefault
            PaidReactionPrivacyPeer
    """

    QUALNAME = "pyrogram.raw.base.PaidReactionPrivacy"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
