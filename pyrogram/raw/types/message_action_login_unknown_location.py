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


class MessageActionLoginUnknownLocation(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``555555F5``

    Parameters:
        title (``str``):
            N/A

        address (``str``):
            N/A

    """

    __slots__: List[str] = ["title", "address"]

    ID = 0x555555f5
    QUALNAME = "types.MessageActionLoginUnknownLocation"

    def __init__(self, *, title: str, address: str) -> None:
        self.title = title  # string
        self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionLoginUnknownLocation":
        # No flags

        title = String.read(b)

        address = String.read(b)

        return MessageActionLoginUnknownLocation(title=title, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(String(self.address))

        return b.getvalue()
