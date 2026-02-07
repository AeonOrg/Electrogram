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


class ReplyInlineMarkup(TLObject):  # type: ignore
    """Bot or inline keyboard

    Constructor of :obj:`~pyrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``224``
        - ID: ``48A30254``

    Parameters:
        rows (List of :obj:`KeyboardButtonRow <pyrogram.raw.base.KeyboardButtonRow>`):
            Bot or inline keyboard rows

    """

    __slots__: List[str] = ["rows"]

    ID = 0x48a30254
    QUALNAME = "types.ReplyInlineMarkup"

    def __init__(self, *, rows: List["raw.base.KeyboardButtonRow"]) -> None:
        self.rows = rows  # Vector<KeyboardButtonRow>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyInlineMarkup":
        # No flags

        rows = TLObject.read(b)

        return ReplyInlineMarkup(rows=rows)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.rows))

        return b.getvalue()
