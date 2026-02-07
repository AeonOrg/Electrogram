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


class MessageMediaToDo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``8A53B014``

    Parameters:
        todo (:obj:`TodoList <pyrogram.raw.base.TodoList>`):
            N/A

        completions (List of :obj:`TodoCompletion <pyrogram.raw.base.TodoCompletion>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["todo", "completions"]

    ID = 0x8a53b014
    QUALNAME = "types.MessageMediaToDo"

    def __init__(self, *, todo: "raw.base.TodoList", completions: Optional[List["raw.base.TodoCompletion"]] = None) -> None:
        self.todo = todo  # TodoList
        self.completions = completions  # flags.0?Vector<TodoCompletion>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaToDo":

        flags = Int.read(b)

        todo = TLObject.read(b)

        completions = TLObject.read(b) if flags & (1 << 0) else []

        return MessageMediaToDo(todo=todo, completions=completions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.completions else 0
        b.write(Int(flags))

        b.write(self.todo.write())

        if self.completions is not None:
            b.write(Vector(self.completions))

        return b.getvalue()
