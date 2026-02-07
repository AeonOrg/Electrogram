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


class SupportName(TLObject):  # type: ignore
    """Localized name for telegram support

    Constructor of :obj:`~pyrogram.raw.base.help.SupportName`.

    Details:
        - Layer: ``224``
        - ID: ``8C05F1C9``

    Parameters:
        name (``str``):
            Localized name

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetSupportName
    """

    __slots__: List[str] = ["name"]

    ID = 0x8c05f1c9
    QUALNAME = "types.help.SupportName"

    def __init__(self, *, name: str) -> None:
        self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SupportName":
        # No flags

        name = String.read(b)

        return SupportName(name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.name))

        return b.getvalue()
