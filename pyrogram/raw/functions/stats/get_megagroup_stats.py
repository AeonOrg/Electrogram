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


class GetMegagroupStats(TLObject):  # type: ignore
    """Get supergroup statistics


    Details:
        - Layer: ``224``
        - ID: ``DCDF8607``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup ID

        dark (``bool``, *optional*):
            Whether to enable dark theme for graph colors

    Returns:
        :obj:`stats.MegagroupStats <pyrogram.raw.base.stats.MegagroupStats>`
    """

    __slots__: List[str] = ["channel", "dark"]

    ID = 0xdcdf8607
    QUALNAME = "functions.stats.GetMegagroupStats"

    def __init__(self, *, channel: "raw.base.InputChannel", dark: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMegagroupStats":

        flags = Int.read(b)

        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(b)

        return GetMegagroupStats(channel=channel, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))

        b.write(self.channel.write())

        return b.getvalue()
