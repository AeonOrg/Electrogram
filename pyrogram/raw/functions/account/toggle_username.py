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


class ToggleUsername(TLObject):  # type: ignore
    """Activate or deactivate a purchased fragment.com username associated to the currently logged-in user.


    Details:
        - Layer: ``224``
        - ID: ``58D6B376``

    Parameters:
        username (``str``):
            Username

        active (``bool``):
            Whether to activate or deactivate it

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["username", "active"]

    ID = 0x58d6b376
    QUALNAME = "functions.account.ToggleUsername"

    def __init__(self, *, username: str, active: bool) -> None:
        self.username = username  # string
        self.active = active  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        # No flags

        username = String.read(b)

        active = Bool.read(b)

        return ToggleUsername(username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.username))

        b.write(Bool(self.active))

        return b.getvalue()
