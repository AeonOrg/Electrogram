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


class InputUserEmpty(TLObject):  # type: ignore
    """Empty constructor, does not define a user.

    Constructor of :obj:`~pyrogram.raw.base.InputUser`.

    Details:
        - Layer: ``224``
        - ID: ``B98886CF``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xb98886cf
    QUALNAME = "types.InputUserEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputUserEmpty":
        # No flags

        return InputUserEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
