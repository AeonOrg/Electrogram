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


class ReactionNotificationsFromContacts(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.ReactionNotificationsFrom`.

    Details:
        - Layer: ``224``
        - ID: ``BAC3A61A``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xbac3a61a
    QUALNAME = "types.ReactionNotificationsFromContacts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionNotificationsFromContacts":
        # No flags

        return ReactionNotificationsFromContacts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
