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


class ChatParticipants(TLObject):  # type: ignore
    """Group members.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipants`.

    Details:
        - Layer: ``224``
        - ID: ``3CBC93F8``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Group identifier

        participants (List of :obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`):
            List of group members

        version (``int`` ``32-bit``):
            Group version number

    """

    __slots__: List[str] = ["chat_id", "participants", "version"]

    ID = 0x3cbc93f8
    QUALNAME = "types.ChatParticipants"

    def __init__(self, *, chat_id: int, participants: List["raw.base.ChatParticipant"], version: int) -> None:
        self.chat_id = chat_id  # long
        self.participants = participants  # Vector<ChatParticipant>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipants":
        # No flags

        chat_id = Long.read(b)

        participants = TLObject.read(b)

        version = Int.read(b)

        return ChatParticipants(chat_id=chat_id, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(Vector(self.participants))

        b.write(Int(self.version))

        return b.getvalue()
