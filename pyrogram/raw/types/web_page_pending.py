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


class WebPagePending(TLObject):  # type: ignore
    """A preview of the webpage is currently being generated

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``224``
        - ID: ``B0D13E47``

    Parameters:
        id (``int`` ``64-bit``):
            ID of preview

        date (``int`` ``32-bit``):
            When was the processing started

        url (``str``, *optional*):
            URL of the webpage

    """

    __slots__: List[str] = ["id", "date", "url"]

    ID = 0xb0d13e47
    QUALNAME = "types.WebPagePending"

    def __init__(self, *, id: int, date: int, url: Optional[str] = None) -> None:
        self.id = id  # long
        self.date = date  # int
        self.url = url  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPagePending":

        flags = Int.read(b)

        id = Long.read(b)

        url = String.read(b) if flags & (1 << 0) else None
        date = Int.read(b)

        return WebPagePending(id=id, date=date, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        b.write(Int(flags))

        b.write(Long(self.id))

        if self.url is not None:
            b.write(String(self.url))

        b.write(Int(self.date))

        return b.getvalue()
