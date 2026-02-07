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


class PassportConfigNotModified(TLObject):  # type: ignore
    """Password configuration not modified

    Constructor of :obj:`~pyrogram.raw.base.help.PassportConfig`.

    Details:
        - Layer: ``224``
        - ID: ``BFB9F457``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPassportConfig
    """

    __slots__: List[str] = []

    ID = 0xbfb9f457
    QUALNAME = "types.help.PassportConfigNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PassportConfigNotModified":
        # No flags

        return PassportConfigNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
