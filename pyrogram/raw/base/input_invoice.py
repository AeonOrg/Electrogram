# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputInvoice = Union["raw.types.InputInvoiceBusinessBotTransferStars", "raw.types.InputInvoiceChatInviteSubscription", "raw.types.InputInvoiceMessage", "raw.types.InputInvoicePremiumAuthCode", "raw.types.InputInvoicePremiumGiftCode", "raw.types.InputInvoicePremiumGiftStars", "raw.types.InputInvoiceSlug", "raw.types.InputInvoiceStarGift", "raw.types.InputInvoiceStarGiftAuctionBid", "raw.types.InputInvoiceStarGiftDropOriginalDetails", "raw.types.InputInvoiceStarGiftPrepaidUpgrade", "raw.types.InputInvoiceStarGiftResale", "raw.types.InputInvoiceStarGiftTransfer", "raw.types.InputInvoiceStarGiftUpgrade", "raw.types.InputInvoiceStars"]


class InputInvoice:  # type: ignore
    """An invoice

    Constructors:
        This base type has 15 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputInvoiceBusinessBotTransferStars
            InputInvoiceChatInviteSubscription
            InputInvoiceMessage
            InputInvoicePremiumAuthCode
            InputInvoicePremiumGiftCode
            InputInvoicePremiumGiftStars
            InputInvoiceSlug
            InputInvoiceStarGift
            InputInvoiceStarGiftAuctionBid
            InputInvoiceStarGiftDropOriginalDetails
            InputInvoiceStarGiftPrepaidUpgrade
            InputInvoiceStarGiftResale
            InputInvoiceStarGiftTransfer
            InputInvoiceStarGiftUpgrade
            InputInvoiceStars
    """

    QUALNAME = "pyrogram.raw.base.InputInvoice"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
