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


class StatsGraphError(TLObject):  # type: ignore
    """An error occurred while generating the statistics graph

    Constructor of :obj:`~pyrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``224``
        - ID: ``BEDC9822``

    Parameters:
        error (``str``):
            The error

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    __slots__: List[str] = ["error"]

    ID = 0xbedc9822
    QUALNAME = "types.StatsGraphError"

    def __init__(self, *, error: str) -> None:
        self.error = error  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraphError":
        # No flags

        error = String.read(b)

        return StatsGraphError(error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.error))

        return b.getvalue()
