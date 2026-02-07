from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputInvoicePremiumGiftCode(TLObject):  # type: ignore
    """Used if the user wishes to start a channel giveaway or send some giftcodes to members of a channel, in exchange for boosts.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``98986C0D``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            Should be populated with inputStorePaymentPremiumGiveaway for giveaways and inputStorePaymentPremiumGiftCode for gifts.

        option (:obj:`PremiumGiftCodeOption <pyrogram.raw.base.PremiumGiftCodeOption>`):
            Should be populated with one of the giveaway options returned by payments.getPremiumGiftCodeOptions, see the giveaways » documentation for more info.

    """

    __slots__: List[str] = ["purpose", "option"]

    ID = 0x98986c0d
    QUALNAME = "types.InputInvoicePremiumGiftCode"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose", option: "raw.base.PremiumGiftCodeOption") -> None:
        self.purpose = purpose  # InputStorePaymentPurpose
        self.option = option  # PremiumGiftCodeOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftCode":
        # No flags

        purpose = TLObject.read(b)

        option = TLObject.read(b)

        return InputInvoicePremiumGiftCode(purpose=purpose, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.purpose.write())

        b.write(self.option.write())

        return b.getvalue()
