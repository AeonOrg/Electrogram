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


class UpdateAttachMenuBots(TLObject):  # type: ignore
    """The list of installed attachment menu entries » has changed, use messages.getAttachMenuBots to fetch the updated list.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``17B7A20B``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x17b7a20b
    QUALNAME = "types.UpdateAttachMenuBots"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateAttachMenuBots":
        # No flags

        return UpdateAttachMenuBots()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
