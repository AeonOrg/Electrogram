# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhoneCallDiscardReason = Union["raw.types.PhoneCallDiscardReasonBusy", "raw.types.PhoneCallDiscardReasonDisconnect", "raw.types.PhoneCallDiscardReasonHangup", "raw.types.PhoneCallDiscardReasonMigrateConferenceCall", "raw.types.PhoneCallDiscardReasonMissed"]


class PhoneCallDiscardReason:  # type: ignore
    """Why was the phone call discarded?

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PhoneCallDiscardReasonBusy
            PhoneCallDiscardReasonDisconnect
            PhoneCallDiscardReasonHangup
            PhoneCallDiscardReasonMigrateConferenceCall
            PhoneCallDiscardReasonMissed
    """

    QUALNAME = "pyrogram.raw.base.PhoneCallDiscardReason"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
