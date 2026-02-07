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


class BotAppNotModified(TLObject):  # type: ignore
    """Bot app info hasn't changed.

    Constructor of :obj:`~pyrogram.raw.base.BotApp`.

    Details:
        - Layer: ``224``
        - ID: ``5DA674B7``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x5da674b7
    QUALNAME = "types.BotAppNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotAppNotModified":
        # No flags

        return BotAppNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
