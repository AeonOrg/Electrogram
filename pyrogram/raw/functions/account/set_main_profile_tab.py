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


class SetMainProfileTab(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5DEE78B0``

    Parameters:
        tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["tab"]

    ID = 0x5dee78b0
    QUALNAME = "functions.account.SetMainProfileTab"

    def __init__(self, *, tab: "raw.base.ProfileTab") -> None:
        self.tab = tab  # ProfileTab

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetMainProfileTab":
        # No flags

        tab = TLObject.read(b)

        return SetMainProfileTab(tab=tab)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.tab.write())

        return b.getvalue()
