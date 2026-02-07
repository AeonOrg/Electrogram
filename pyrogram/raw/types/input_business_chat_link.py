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


class InputBusinessChatLink(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.InputBusinessChatLink`.

    Details:
        - Layer: ``224``
        - ID: ``11679FA7``

    Parameters:
        message (``str``):


        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        title (``str``, *optional*):


    """

    __slots__: List[str] = ["message", "entities", "title"]

    ID = 0x11679fa7
    QUALNAME = "types.InputBusinessChatLink"

    def __init__(self, *, message: str, entities: Optional[List["raw.base.MessageEntity"]] = None, title: Optional[str] = None) -> None:
        self.message = message  # string
        self.entities = entities  # flags.0?Vector<MessageEntity>
        self.title = title  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessChatLink":

        flags = Int.read(b)

        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 0) else []

        title = String.read(b) if flags & (1 << 1) else None
        return InputBusinessChatLink(message=message, entities=entities, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.entities else 0
        flags |= (1 << 1) if self.title is not None else 0
        b.write(Int(flags))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.title is not None:
            b.write(String(self.title))

        return b.getvalue()
