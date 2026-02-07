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


class ChatReactionsNone(TLObject):  # type: ignore
    """No reactions are allowed

    Constructor of :obj:`~pyrogram.raw.base.ChatReactions`.

    Details:
        - Layer: ``224``
        - ID: ``EAFC32BC``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xeafc32bc
    QUALNAME = "types.ChatReactionsNone"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsNone":
        # No flags

        return ChatReactionsNone()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
