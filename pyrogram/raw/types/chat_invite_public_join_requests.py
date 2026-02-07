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


class ChatInvitePublicJoinRequests(TLObject):  # type: ignore
    """Used in updates and in the channel log to indicate when a user is requesting to join or has joined a discussion group

    Constructor of :obj:`~pyrogram.raw.base.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``ED107AB7``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ExportChatInvite
    """

    __slots__: List[str] = []

    ID = 0xed107ab7
    QUALNAME = "types.ChatInvitePublicJoinRequests"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvitePublicJoinRequests":
        # No flags

        return ChatInvitePublicJoinRequests()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
