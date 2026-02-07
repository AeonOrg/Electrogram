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


class MessageActionChatEditTitle(TLObject):  # type: ignore
    """Group name changed.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B5A1CE5A``

    Parameters:
        title (``str``):
            New group name

    """

    __slots__: List[str] = ["title"]

    ID = 0xb5a1ce5a
    QUALNAME = "types.MessageActionChatEditTitle"

    def __init__(self, *, title: str) -> None:
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatEditTitle":
        # No flags

        title = String.read(b)

        return MessageActionChatEditTitle(title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        return b.getvalue()
