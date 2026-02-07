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


class UpdateWebViewResultSent(TLObject):  # type: ignore
    """Indicates to a bot that a webview was closed and an inline message was sent on behalf of the user using messages.sendWebViewResultMessage

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1592B79D``

    Parameters:
        query_id (``int`` ``64-bit``):
            Web app interaction ID

    """

    __slots__: List[str] = ["query_id"]

    ID = 0x1592b79d
    QUALNAME = "types.UpdateWebViewResultSent"

    def __init__(self, *, query_id: int) -> None:
        self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebViewResultSent":
        # No flags

        query_id = Long.read(b)

        return UpdateWebViewResultSent(query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        return b.getvalue()
