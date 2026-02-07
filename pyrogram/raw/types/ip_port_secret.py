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


class IpPortSecret(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.IpPort`.

    Details:
        - Layer: ``224``
        - ID: ``37982646``

    Parameters:
        ipv4 (``int`` ``32-bit``):
            N/A

        port (``int`` ``32-bit``):
            N/A

        secret (``bytes``):
            N/A

    """

    __slots__: List[str] = ["ipv4", "port", "secret"]

    ID = 0x37982646
    QUALNAME = "types.IpPortSecret"

    def __init__(self, *, ipv4: int, port: int, secret: bytes) -> None:
        self.ipv4 = ipv4  # int
        self.port = port  # int
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "IpPortSecret":
        # No flags

        ipv4 = Int.read(b)

        port = Int.read(b)

        secret = Bytes.read(b)

        return IpPortSecret(ipv4=ipv4, port=port, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.ipv4))

        b.write(Int(self.port))

        b.write(Bytes(self.secret))

        return b.getvalue()
