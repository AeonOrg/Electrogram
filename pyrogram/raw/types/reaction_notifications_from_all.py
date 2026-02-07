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


class ReactionNotificationsFromAll(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.ReactionNotificationsFrom`.

    Details:
        - Layer: ``224``
        - ID: ``4B9E22A0``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x4b9e22a0
    QUALNAME = "types.ReactionNotificationsFromAll"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionNotificationsFromAll":
        # No flags

        return ReactionNotificationsFromAll()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
