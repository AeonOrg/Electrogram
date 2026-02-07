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


class ChatParticipantsForbidden(TLObject):  # type: ignore
    """Info on members is unavailable

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipants`.

    Details:
        - Layer: ``224``
        - ID: ``8763D3E1``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Group ID

        self_participant (:obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`, *optional*):
            Info about the group membership of the current user

    """

    __slots__: List[str] = ["chat_id", "self_participant"]

    ID = 0x8763d3e1
    QUALNAME = "types.ChatParticipantsForbidden"

    def __init__(self, *, chat_id: int, self_participant: "raw.base.ChatParticipant" = None) -> None:
        self.chat_id = chat_id  # long
        self.self_participant = self_participant  # flags.0?ChatParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantsForbidden":

        flags = Int.read(b)

        chat_id = Long.read(b)

        self_participant = TLObject.read(b) if flags & (1 << 0) else None

        return ChatParticipantsForbidden(chat_id=chat_id, self_participant=self_participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.self_participant is not None else 0
        b.write(Int(flags))

        b.write(Long(self.chat_id))

        if self.self_participant is not None:
            b.write(self.self_participant.write())

        return b.getvalue()
