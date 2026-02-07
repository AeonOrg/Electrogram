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


class UpdatePaidReactionPrivacy(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8B725FCE``

    Parameters:
        private (:obj:`PaidReactionPrivacy <pyrogram.raw.base.PaidReactionPrivacy>`):
            N/A

    """

    __slots__: List[str] = ["private"]

    ID = 0x8b725fce
    QUALNAME = "types.UpdatePaidReactionPrivacy"

    def __init__(self, *, private: "raw.base.PaidReactionPrivacy") -> None:
        self.private = private  # PaidReactionPrivacy

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePaidReactionPrivacy":
        # No flags

        private = TLObject.read(b)

        return UpdatePaidReactionPrivacy(private=private)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.private.write())

        return b.getvalue()
