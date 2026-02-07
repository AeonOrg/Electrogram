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


class GetStatsURL(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``812C2AE6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        params (``str``):
            N/A

        dark (``bool``, *optional*):
            N/A

    Returns:
        :obj:`StatsURL <pyrogram.raw.base.StatsURL>`
    """

    __slots__: List[str] = ["peer", "params", "dark"]

    ID = 0x812c2ae6
    QUALNAME = "functions.messages.GetStatsURL"

    def __init__(self, *, peer: "raw.base.InputPeer", params: str, dark: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.params = params  # string
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStatsURL":

        flags = Int.read(b)

        dark = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        params = String.read(b)

        return GetStatsURL(peer=peer, params=params, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.params))

        return b.getvalue()
