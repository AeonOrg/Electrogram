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


class InputChatThemeUniqueGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChatTheme`.

    Details:
        - Layer: ``224``
        - ID: ``87E5DFE4``

    Parameters:
        slug (``str``):
            N/A

    """

    __slots__: List[str] = ["slug"]

    ID = 0x87e5dfe4
    QUALNAME = "types.InputChatThemeUniqueGift"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatThemeUniqueGift":
        # No flags

        slug = String.read(b)

        return InputChatThemeUniqueGift(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
