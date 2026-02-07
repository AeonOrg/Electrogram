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


class ExportedStoryLink(TLObject):  # type: ignore
    """Represents a story deep link.

    Constructor of :obj:`~pyrogram.raw.base.ExportedStoryLink`.

    Details:
        - Layer: ``224``
        - ID: ``3FC9053B``

    Parameters:
        link (``str``):
            The story deep link.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.ExportStoryLink
    """

    __slots__: List[str] = ["link"]

    ID = 0x3fc9053b
    QUALNAME = "types.ExportedStoryLink"

    def __init__(self, *, link: str) -> None:
        self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedStoryLink":
        # No flags

        link = String.read(b)

        return ExportedStoryLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.link))

        return b.getvalue()
