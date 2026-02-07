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


class InputMediaTodo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``9FC55FDE``

    Parameters:
        todo (:obj:`TodoList <pyrogram.raw.base.TodoList>`):
            N/A

    """

    __slots__: List[str] = ["todo"]

    ID = 0x9fc55fde
    QUALNAME = "types.InputMediaTodo"

    def __init__(self, *, todo: "raw.base.TodoList") -> None:
        self.todo = todo  # TodoList

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaTodo":
        # No flags

        todo = TLObject.read(b)

        return InputMediaTodo(todo=todo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.todo.write())

        return b.getvalue()
