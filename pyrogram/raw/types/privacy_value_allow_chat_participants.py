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


class PrivacyValueAllowChatParticipants(TLObject):  # type: ignore
    """Allow all participants of certain chats

    Constructor of :obj:`~pyrogram.raw.base.PrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``6B134E8E``

    Parameters:
        chats (List of ``int`` ``64-bit``):
            Allowed chats

    """

    __slots__: List[str] = ["chats"]

    ID = 0x6b134e8e
    QUALNAME = "types.PrivacyValueAllowChatParticipants"

    def __init__(self, *, chats: List[int]) -> None:
        self.chats = chats  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueAllowChatParticipants":
        # No flags

        chats = TLObject.read(b, Long)

        return PrivacyValueAllowChatParticipants(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.chats, Long))

        return b.getvalue()
