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


class MessageActionTodoCompletions(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``CC7C5C89``

    Parameters:
        completed (List of ``int`` ``32-bit``):
            N/A

        incompleted (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["completed", "incompleted"]

    ID = 0xcc7c5c89
    QUALNAME = "types.MessageActionTodoCompletions"

    def __init__(self, *, completed: List[int], incompleted: List[int]) -> None:
        self.completed = completed  # Vector<int>
        self.incompleted = incompleted  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTodoCompletions":
        # No flags

        completed = TLObject.read(b, Int)

        incompleted = TLObject.read(b, Int)

        return MessageActionTodoCompletions(completed=completed, incompleted=incompleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.completed, Int))

        b.write(Vector(self.incompleted, Int))

        return b.getvalue()
