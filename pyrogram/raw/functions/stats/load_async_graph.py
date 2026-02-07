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


class LoadAsyncGraph(TLObject):  # type: ignore
    """Load channel statistics graph asynchronously


    Details:
        - Layer: ``224``
        - ID: ``621D5FA0``

    Parameters:
        token (``str``):
            Graph token from statsGraphAsync constructor

        x (``int`` ``64-bit``, *optional*):
            Zoom value, if required

    Returns:
        :obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`
    """

    __slots__: List[str] = ["token", "x"]

    ID = 0x621d5fa0
    QUALNAME = "functions.stats.LoadAsyncGraph"

    def __init__(self, *, token: str, x: Optional[int] = None) -> None:
        self.token = token  # string
        self.x = x  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoadAsyncGraph":

        flags = Int.read(b)

        token = String.read(b)

        x = Long.read(b) if flags & (1 << 0) else None
        return LoadAsyncGraph(token=token, x=x)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.x is not None else 0
        b.write(Int(flags))

        b.write(String(self.token))

        if self.x is not None:
            b.write(Long(self.x))

        return b.getvalue()
