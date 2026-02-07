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


class UpdateQuickReplies(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F9470AB2``

    Parameters:
        quick_replies (List of :obj:`QuickReply <pyrogram.raw.base.QuickReply>`):


    """

    __slots__: List[str] = ["quick_replies"]

    ID = 0xf9470ab2
    QUALNAME = "types.UpdateQuickReplies"

    def __init__(self, *, quick_replies: List["raw.base.QuickReply"]) -> None:
        self.quick_replies = quick_replies  # Vector<QuickReply>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateQuickReplies":
        # No flags

        quick_replies = TLObject.read(b)

        return UpdateQuickReplies(quick_replies=quick_replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.quick_replies))

        return b.getvalue()
