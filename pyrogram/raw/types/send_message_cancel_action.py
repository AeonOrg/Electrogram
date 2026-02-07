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


class SendMessageCancelAction(TLObject):  # type: ignore
    """Invalidate all previous action updates. E.g. when user deletes entered text or aborts a video upload.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``FD5EC8F5``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xfd5ec8f5
    QUALNAME = "types.SendMessageCancelAction"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageCancelAction":
        # No flags

        return SendMessageCancelAction()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
