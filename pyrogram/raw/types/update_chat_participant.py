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


class UpdateChatParticipant(TLObject):  # type: ignore
    """A user has joined or left a specific chat

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D087663A``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

        date (``int`` ``32-bit``):
            When did this event occur

        actor_id (``int`` ``64-bit``):
            User that triggered the change (inviter, admin that kicked the user, or the even the user_id itself)

        user_id (``int`` ``64-bit``):
            User that was affected by the change

        qts (``int`` ``32-bit``):
            New qts value, see updates » for more info.

        prev_participant (:obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`, *optional*):
            Previous participant info (empty if this participant just joined)

        new_participant (:obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`, *optional*):
            New participant info (empty if this participant just left)

        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`, *optional*):
            The invite that was used to join the group

    """

    __slots__: List[str] = ["chat_id", "date", "actor_id", "user_id", "qts", "prev_participant", "new_participant", "invite"]

    ID = 0xd087663a
    QUALNAME = "types.UpdateChatParticipant"

    def __init__(self, *, chat_id: int, date: int, actor_id: int, user_id: int, qts: int, prev_participant: "raw.base.ChatParticipant" = None, new_participant: "raw.base.ChatParticipant" = None, invite: "raw.base.ExportedChatInvite" = None) -> None:
        self.chat_id = chat_id  # long
        self.date = date  # int
        self.actor_id = actor_id  # long
        self.user_id = user_id  # long
        self.qts = qts  # int
        self.prev_participant = prev_participant  # flags.0?ChatParticipant
        self.new_participant = new_participant  # flags.1?ChatParticipant
        self.invite = invite  # flags.2?ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipant":

        flags = Int.read(b)

        chat_id = Long.read(b)

        date = Int.read(b)

        actor_id = Long.read(b)

        user_id = Long.read(b)

        prev_participant = TLObject.read(b) if flags & (1 << 0) else None

        new_participant = TLObject.read(b) if flags & (1 << 1) else None

        invite = TLObject.read(b) if flags & (1 << 2) else None

        qts = Int.read(b)

        return UpdateChatParticipant(chat_id=chat_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prev_participant is not None else 0
        flags |= (1 << 1) if self.new_participant is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        b.write(Int(flags))

        b.write(Long(self.chat_id))

        b.write(Int(self.date))

        b.write(Long(self.actor_id))

        b.write(Long(self.user_id))

        if self.prev_participant is not None:
            b.write(self.prev_participant.write())

        if self.new_participant is not None:
            b.write(self.new_participant.write())

        if self.invite is not None:
            b.write(self.invite.write())

        b.write(Int(self.qts))

        return b.getvalue()
