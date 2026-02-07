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


class UpdateBotChatInviteRequester(TLObject):  # type: ignore
    """Someone has requested to join a chat or channel (bots only, users will receive an updatePendingJoinRequests, instead)

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``11DFA986``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The chat or channel in question

        date (``int`` ``32-bit``):
            When was the join request » made

        user_id (``int`` ``64-bit``):
            The user ID that is asking to join the chat or channel

        about (``str``):
            Bio of the user

        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            Chat invite link that was used by the user to send the join request »

        qts (``int`` ``32-bit``):
            QTS event sequence identifier

    """

    __slots__: List[str] = ["peer", "date", "user_id", "about", "invite", "qts"]

    ID = 0x11dfa986
    QUALNAME = "types.UpdateBotChatInviteRequester"

    def __init__(self, *, peer: "raw.base.Peer", date: int, user_id: int, about: str, invite: "raw.base.ExportedChatInvite", qts: int) -> None:
        self.peer = peer  # Peer
        self.date = date  # int
        self.user_id = user_id  # long
        self.about = about  # string
        self.invite = invite  # ExportedChatInvite
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatInviteRequester":
        # No flags

        peer = TLObject.read(b)

        date = Int.read(b)

        user_id = Long.read(b)

        about = String.read(b)

        invite = TLObject.read(b)

        qts = Int.read(b)

        return UpdateBotChatInviteRequester(peer=peer, date=date, user_id=user_id, about=about, invite=invite, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.date))

        b.write(Long(self.user_id))

        b.write(String(self.about))

        b.write(self.invite.write())

        b.write(Int(self.qts))

        return b.getvalue()
