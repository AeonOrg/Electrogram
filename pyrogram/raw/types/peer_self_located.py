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


class PeerSelfLocated(TLObject):  # type: ignore
    """Current peer

    Constructor of :obj:`~pyrogram.raw.base.PeerLocated`.

    Details:
        - Layer: ``224``
        - ID: ``F8EC284B``

    Parameters:
        expires (``int`` ``32-bit``):
            Expiry of geolocation info for current peer

    """

    __slots__: List[str] = ["expires"]

    ID = 0xf8ec284b
    QUALNAME = "types.PeerSelfLocated"

    def __init__(self, *, expires: int) -> None:
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSelfLocated":
        # No flags

        expires = Int.read(b)

        return PeerSelfLocated(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.expires))

        return b.getvalue()
