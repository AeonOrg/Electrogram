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


class AllStoriesNotModified(TLObject):  # type: ignore
    """The list of active (or active and hidden) stories has not changed.

    Constructor of :obj:`~pyrogram.raw.base.stories.AllStories`.

    Details:
        - Layer: ``224``
        - ID: ``1158FE3E``

    Parameters:
        state (``str``):
            State to use to ask for updates

        stealth_mode (:obj:`StoriesStealthMode <pyrogram.raw.base.StoriesStealthMode>`):
            Current stealth mode information

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetAllStories
    """

    __slots__: List[str] = ["state", "stealth_mode"]

    ID = 0x1158fe3e
    QUALNAME = "types.stories.AllStoriesNotModified"

    def __init__(self, *, state: str, stealth_mode: "raw.base.StoriesStealthMode") -> None:
        self.state = state  # string
        self.stealth_mode = stealth_mode  # StoriesStealthMode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStoriesNotModified":

        flags = Int.read(b)

        state = String.read(b)

        stealth_mode = TLObject.read(b)

        return AllStoriesNotModified(state=state, stealth_mode=stealth_mode)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0

        b.write(Int(flags))

        b.write(String(self.state))

        b.write(self.stealth_mode.write())

        return b.getvalue()
