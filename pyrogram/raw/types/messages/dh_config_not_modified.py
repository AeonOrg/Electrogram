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


class DhConfigNotModified(TLObject):  # type: ignore
    """Configuring parameters did not change.

    Constructor of :obj:`~pyrogram.raw.base.messages.DhConfig`.

    Details:
        - Layer: ``224``
        - ID: ``C0E24635``

    Parameters:
        random (``bytes``):
            Random sequence of bytes of assigned length

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDhConfig
    """

    __slots__: List[str] = ["random"]

    ID = 0xc0e24635
    QUALNAME = "types.messages.DhConfigNotModified"

    def __init__(self, *, random: bytes) -> None:
        self.random = random  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhConfigNotModified":
        # No flags

        random = Bytes.read(b)

        return DhConfigNotModified(random=random)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.random))

        return b.getvalue()
