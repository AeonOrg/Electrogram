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


class JsonArray(TLObject):  # type: ignore
    """JSON array

    Constructor of :obj:`~pyrogram.raw.base.JSONValue`.

    Details:
        - Layer: ``224``
        - ID: ``F7444763``

    Parameters:
        value (List of :obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            JSON values

    """

    __slots__: List[str] = ["value"]

    ID = 0xf7444763
    QUALNAME = "types.JsonArray"

    def __init__(self, *, value: List["raw.base.JSONValue"]) -> None:
        self.value = value  # Vector<JSONValue>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonArray":
        # No flags

        value = TLObject.read(b)

        return JsonArray(value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.value))

        return b.getvalue()
