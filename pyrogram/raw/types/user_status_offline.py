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


class UserStatusOffline(TLObject):  # type: ignore
    """The user's offline status.

    Constructor of :obj:`~pyrogram.raw.base.UserStatus`.

    Details:
        - Layer: ``224``
        - ID: ``8C703F``

    Parameters:
        was_online (``int`` ``32-bit``):
            Time the user was last seen online

    """

    __slots__: List[str] = ["was_online"]

    ID = 0x8c703f
    QUALNAME = "types.UserStatusOffline"

    def __init__(self, *, was_online: int) -> None:
        self.was_online = was_online  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusOffline":
        # No flags

        was_online = Int.read(b)

        return UserStatusOffline(was_online=was_online)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.was_online))

        return b.getvalue()
