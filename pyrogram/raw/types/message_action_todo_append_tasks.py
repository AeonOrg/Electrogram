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


class MessageActionTodoAppendTasks(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``C7EDBC83``

    Parameters:
        list (List of :obj:`TodoItem <pyrogram.raw.base.TodoItem>`):
            N/A

    """

    __slots__: List[str] = ["list"]

    ID = 0xc7edbc83
    QUALNAME = "types.MessageActionTodoAppendTasks"

    def __init__(self, *, list: List["raw.base.TodoItem"]) -> None:
        self.list = list  # Vector<TodoItem>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTodoAppendTasks":
        # No flags

        list = TLObject.read(b)

        return MessageActionTodoAppendTasks(list=list)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.list))

        return b.getvalue()
