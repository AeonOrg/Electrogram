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


class InputCollectiblePhone(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.InputCollectible`.

    Details:
        - Layer: ``224``
        - ID: ``A2E214A4``

    Parameters:
        phone (``str``):


    """

    __slots__: List[str] = ["phone"]

    ID = 0xa2e214a4
    QUALNAME = "types.InputCollectiblePhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCollectiblePhone":
        # No flags

        phone = String.read(b)

        return InputCollectiblePhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone))

        return b.getvalue()
