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


class GetGroupsForDiscussion(TLObject):  # type: ignore
    """Get all groups that can be used as discussion groups.


    Details:
        - Layer: ``224``
        - ID: ``F5DAD378``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = []

    ID = 0xf5dad378
    QUALNAME = "functions.channels.GetGroupsForDiscussion"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupsForDiscussion":
        # No flags

        return GetGroupsForDiscussion()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
