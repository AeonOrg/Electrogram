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


class InputCheckPasswordEmpty(TLObject):  # type: ignore
    """There is no password

    Constructor of :obj:`~pyrogram.raw.base.InputCheckPasswordSRP`.

    Details:
        - Layer: ``224``
        - ID: ``9880F658``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x9880f658
    QUALNAME = "types.InputCheckPasswordEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCheckPasswordEmpty":
        # No flags

        return InputCheckPasswordEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
