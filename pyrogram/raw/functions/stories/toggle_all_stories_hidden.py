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


class ToggleAllStoriesHidden(TLObject):  # type: ignore
    """Hide the active stories of a specific peer, preventing them from being displayed on the action bar on the homescreen.


    Details:
        - Layer: ``224``
        - ID: ``7C2557C4``

    Parameters:
        hidden (``bool``):
            Whether to hide or unhide all active stories of the peer

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hidden"]

    ID = 0x7c2557c4
    QUALNAME = "functions.stories.ToggleAllStoriesHidden"

    def __init__(self, *, hidden: bool) -> None:
        self.hidden = hidden  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleAllStoriesHidden":
        # No flags

        hidden = Bool.read(b)

        return ToggleAllStoriesHidden(hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bool(self.hidden))

        return b.getvalue()
