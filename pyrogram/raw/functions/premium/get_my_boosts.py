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


class GetMyBoosts(TLObject):  # type: ignore
    """Obtain which peers are we currently boosting, and how many boost slots we have left.


    Details:
        - Layer: ``224``
        - ID: ``BE77B4A``

    Parameters:
        No parameters required.

    Returns:
        :obj:`premium.MyBoosts <pyrogram.raw.base.premium.MyBoosts>`
    """

    __slots__: List[str] = []

    ID = 0xbe77b4a
    QUALNAME = "functions.premium.GetMyBoosts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMyBoosts":
        # No flags

        return GetMyBoosts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
