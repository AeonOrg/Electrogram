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


class ChannelDifferenceEmpty(TLObject):  # type: ignore
    """There are no new updates

    Constructor of :obj:`~pyrogram.raw.base.updates.ChannelDifference`.

    Details:
        - Layer: ``224``
        - ID: ``3E11AFFB``

    Parameters:
        pts (``int`` ``32-bit``):
            The latest PTS

        final (``bool``, *optional*):
            Whether there are more updates that must be fetched (always false)

        timeout (``int`` ``32-bit``, *optional*):
            Clients are supposed to refetch the channel difference after timeout seconds have elapsed

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetChannelDifference
    """

    __slots__: List[str] = ["pts", "final", "timeout"]

    ID = 0x3e11affb
    QUALNAME = "types.updates.ChannelDifferenceEmpty"

    def __init__(self, *, pts: int, final: Optional[bool] = None, timeout: Optional[int] = None) -> None:
        self.pts = pts  # int
        self.final = final  # flags.0?true
        self.timeout = timeout  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelDifferenceEmpty":

        flags = Int.read(b)

        final = True if flags & (1 << 0) else False
        pts = Int.read(b)

        timeout = Int.read(b) if flags & (1 << 1) else None
        return ChannelDifferenceEmpty(pts=pts, final=final, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        b.write(Int(flags))

        b.write(Int(self.pts))

        if self.timeout is not None:
            b.write(Int(self.timeout))

        return b.getvalue()
