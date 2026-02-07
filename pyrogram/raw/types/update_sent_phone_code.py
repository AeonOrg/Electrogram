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


class UpdateSentPhoneCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``504AA18F``

    Parameters:
        sent_code (:obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`):
            N/A

    """

    __slots__: List[str] = ["sent_code"]

    ID = 0x504aa18f
    QUALNAME = "types.UpdateSentPhoneCode"

    def __init__(self, *, sent_code: "raw.base.auth.SentCode") -> None:
        self.sent_code = sent_code  # auth.SentCode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSentPhoneCode":
        # No flags

        sent_code = TLObject.read(b)

        return UpdateSentPhoneCode(sent_code=sent_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.sent_code.write())

        return b.getvalue()
