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


class ToggleSponsoredMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``B9D9A38D``

    Parameters:
        enabled (``bool``):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["enabled"]

    ID = 0xb9d9a38d
    QUALNAME = "functions.account.ToggleSponsoredMessages"

    def __init__(self, *, enabled: bool) -> None:
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleSponsoredMessages":
        # No flags

        enabled = Bool.read(b)

        return ToggleSponsoredMessages(enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bool(self.enabled))

        return b.getvalue()
