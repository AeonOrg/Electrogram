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


class PasswordKdfAlgoUnknown(TLObject):  # type: ignore
    """Unknown KDF (most likely, the client is outdated and does not support the specified KDF algorithm)

    Constructor of :obj:`~pyrogram.raw.base.PasswordKdfAlgo`.

    Details:
        - Layer: ``224``
        - ID: ``D45AB096``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd45ab096
    QUALNAME = "types.PasswordKdfAlgoUnknown"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordKdfAlgoUnknown":
        # No flags

        return PasswordKdfAlgoUnknown()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
