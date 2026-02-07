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


class NoAppUpdate(TLObject):  # type: ignore
    """No updates are available for the application.

    Constructor of :obj:`~pyrogram.raw.base.help.AppUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``C45A6536``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppUpdate
    """

    __slots__: List[str] = []

    ID = 0xc45a6536
    QUALNAME = "types.help.NoAppUpdate"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NoAppUpdate":
        # No flags

        return NoAppUpdate()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
