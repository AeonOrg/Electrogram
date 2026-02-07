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


class MessageActionCustomAction(TLObject):  # type: ignore
    """Custom action (most likely not supported by the current layer, an upgrade might be needed)

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``FAE69F56``

    Parameters:
        message (``str``):
            Action message

    """

    __slots__: List[str] = ["message"]

    ID = 0xfae69f56
    QUALNAME = "types.MessageActionCustomAction"

    def __init__(self, *, message: str) -> None:
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionCustomAction":
        # No flags

        message = String.read(b)

        return MessageActionCustomAction(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.message))

        return b.getvalue()
