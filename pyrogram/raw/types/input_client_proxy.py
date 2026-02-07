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


class InputClientProxy(TLObject):  # type: ignore
    """Info about an MTProxy used to connect.

    Constructor of :obj:`~pyrogram.raw.base.InputClientProxy`.

    Details:
        - Layer: ``224``
        - ID: ``75588B3F``

    Parameters:
        address (``str``):
            Proxy address

        port (``int`` ``32-bit``):
            Proxy port

    """

    __slots__: List[str] = ["address", "port"]

    ID = 0x75588b3f
    QUALNAME = "types.InputClientProxy"

    def __init__(self, *, address: str, port: int) -> None:
        self.address = address  # string
        self.port = port  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputClientProxy":
        # No flags

        address = String.read(b)

        port = Int.read(b)

        return InputClientProxy(address=address, port=port)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.address))

        b.write(Int(self.port))

        return b.getvalue()
