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


class SendConfirmPhoneCode(TLObject):  # type: ignore
    """Send confirmation code to cancel account deletion, for more info click here »


    Details:
        - Layer: ``224``
        - ID: ``1B3FAA88``

    Parameters:
        hash (``str``):
            The hash from the service notification, for more info click here »

        settings (:obj:`CodeSettings <pyrogram.raw.base.CodeSettings>`):
            Phone code settings

    Returns:
        :obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`
    """

    __slots__: List[str] = ["hash", "settings"]

    ID = 0x1b3faa88
    QUALNAME = "functions.account.SendConfirmPhoneCode"

    def __init__(self, *, hash: str, settings: "raw.base.CodeSettings") -> None:
        self.hash = hash  # string
        self.settings = settings  # CodeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendConfirmPhoneCode":
        # No flags

        hash = String.read(b)

        settings = TLObject.read(b)

        return SendConfirmPhoneCode(hash=hash, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.hash))

        b.write(self.settings.write())

        return b.getvalue()
