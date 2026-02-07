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


class JsonNumber(TLObject):  # type: ignore
    """JSON numeric value

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``224``
        - ID: ``2BE0DFA4``

    Parameters:
        value (``float`` ``64-bit``):
            Value

    """

    __slots__: List[str] = ["value"]

    ID = 0x2be0dfa4
    QUALNAME = "types.JsonNumber"

    def __init__(self, *, value: float) -> None:
        self.value = value  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonNumber":
        # No flags

        value = Double.read(b)

        return JsonNumber(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Double(self.value))

        return b.getvalue()
