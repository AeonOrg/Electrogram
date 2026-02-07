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


class StoryViews(TLObject):  # type: ignore
    """Reaction and view counters for a list of stories

    Constructor of :obj:`~pyrogram.raw.base.stories.StoryViews`.

    Details:
        - Layer: ``224``
        - ID: ``DE9EED1D``

    Parameters:
        views (List of :obj:`StoryViews <pyrogram.raw.base.StoryViews>`):
            View date and reaction information of multiple stories

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoriesViews
    """

    __slots__: List[str] = ["views", "users"]

    ID = 0xde9eed1d
    QUALNAME = "types.stories.StoryViews"

    def __init__(self, *, views: List["raw.base.StoryViews"], users: List["raw.base.User"]) -> None:
        self.views = views  # Vector<StoryViews>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        # No flags

        views = TLObject.read(b)

        users = TLObject.read(b)

        return StoryViews(views=views, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.views))

        b.write(Vector(self.users))

        return b.getvalue()
