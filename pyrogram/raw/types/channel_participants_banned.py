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


class ChannelParticipantsBanned(TLObject):  # type: ignore
    """Fetch only banned participants

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipantsFilter`.

    Details:
        - Layer: ``224``
        - ID: ``1427A5E1``

    Parameters:
        q (``str``):
            Optional filter for searching banned participants by name (otherwise empty)

    """

    __slots__: List[str] = ["q"]

    ID = 0x1427a5e1
    QUALNAME = "types.ChannelParticipantsBanned"

    def __init__(self, *, q: str) -> None:
        self.q = q  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantsBanned":
        # No flags

        q = String.read(b)

        return ChannelParticipantsBanned(q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.q))

        return b.getvalue()
