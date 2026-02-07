# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputStorePaymentPurpose = Union["raw.types.InputStorePaymentAuthCode", "raw.types.InputStorePaymentGiftPremium", "raw.types.InputStorePaymentPremiumGiftCode", "raw.types.InputStorePaymentPremiumGiveaway", "raw.types.InputStorePaymentPremiumSubscription", "raw.types.InputStorePaymentStarsGift", "raw.types.InputStorePaymentStarsGiveaway", "raw.types.InputStorePaymentStarsTopup"]


class InputStorePaymentPurpose:  # type: ignore
    """Info about a Telegram Premium purchase

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStorePaymentAuthCode
            InputStorePaymentGiftPremium
            InputStorePaymentPremiumGiftCode
            InputStorePaymentPremiumGiveaway
            InputStorePaymentPremiumSubscription
            InputStorePaymentStarsGift
            InputStorePaymentStarsGiveaway
            InputStorePaymentStarsTopup
    """

    QUALNAME = "pyrogram.raw.base.InputStorePaymentPurpose"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
