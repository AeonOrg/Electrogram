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


class DeleteQuickReplyShortcut(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``3CC04740``

    Parameters:
        shortcut_id (``int`` ``32-bit``):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["shortcut_id"]

    ID = 0x3cc04740
    QUALNAME = "functions.messages.DeleteQuickReplyShortcut"

    def __init__(self, *, shortcut_id: int) -> None:
        self.shortcut_id = shortcut_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteQuickReplyShortcut":
        # No flags

        shortcut_id = Int.read(b)

        return DeleteQuickReplyShortcut(shortcut_id=shortcut_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.shortcut_id))

        return b.getvalue()
