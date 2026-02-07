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


class MessageEntityTextUrl(TLObject):  # type: ignore
    """Message entity representing a text url: for in-text urls like https://google.com use messageEntityUrl.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``76A6D327``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset of message entity within message (in UTF-16 code units)

        length (``int`` ``32-bit``):
            Length of message entity within message (in UTF-16 code units)

        url (``str``):
            The actual URL

    """

    __slots__: List[str] = ["offset", "length", "url"]

    ID = 0x76a6d327
    QUALNAME = "types.MessageEntityTextUrl"

    def __init__(self, *, offset: int, length: int, url: str) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityTextUrl":
        # No flags

        offset = Int.read(b)

        length = Int.read(b)

        url = String.read(b)

        return MessageEntityTextUrl(offset=offset, length=length, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.offset))

        b.write(Int(self.length))

        b.write(String(self.url))

        return b.getvalue()
