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


class UpdateSettings(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``93FA0BF``

    Parameters:
        allow_international (``bool``, *optional*):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["allow_international"]

    ID = 0x93fa0bf
    QUALNAME = "functions.smsjobs.UpdateSettings"

    def __init__(self, *, allow_international: Optional[bool] = None) -> None:
        self.allow_international = allow_international  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSettings":

        flags = Int.read(b)

        allow_international = True if flags & (1 << 0) else False
        return UpdateSettings(allow_international=allow_international)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_international else 0
        b.write(Int(flags))

        return b.getvalue()
