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


class UpdateDeleteQuickReplyMessages(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``566FE7CD``

    Parameters:
        shortcut_id (``int`` ``32-bit``):


        messages (List of ``int`` ``32-bit``):


    """

    __slots__: List[str] = ["shortcut_id", "messages"]

    ID = 0x566fe7cd
    QUALNAME = "types.UpdateDeleteQuickReplyMessages"

    def __init__(self, *, shortcut_id: int, messages: List[int]) -> None:
        self.shortcut_id = shortcut_id  # int
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteQuickReplyMessages":
        # No flags

        shortcut_id = Int.read(b)

        messages = TLObject.read(b, Int)

        return UpdateDeleteQuickReplyMessages(shortcut_id=shortcut_id, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.shortcut_id))

        b.write(Vector(self.messages, Int))

        return b.getvalue()
