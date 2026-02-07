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


class ChannelAdminLogEventActionParticipantJoinByInvite(TLObject):  # type: ignore
    """A user joined the supergroup/channel using a specific invite link

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``FE9FC158``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            The invite link used to join the supergroup/channel

        via_chatlist (``bool``, *optional*):
            The participant joined by importing a chat folder deep link ».

    """

    __slots__: List[str] = ["invite", "via_chatlist"]

    ID = 0xfe9fc158
    QUALNAME = "types.ChannelAdminLogEventActionParticipantJoinByInvite"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", via_chatlist: Optional[bool] = None) -> None:
        self.invite = invite  # ExportedChatInvite
        self.via_chatlist = via_chatlist  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantJoinByInvite":

        flags = Int.read(b)

        via_chatlist = True if flags & (1 << 0) else False
        invite = TLObject.read(b)

        return ChannelAdminLogEventActionParticipantJoinByInvite(invite=invite, via_chatlist=via_chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_chatlist else 0
        b.write(Int(flags))

        b.write(self.invite.write())

        return b.getvalue()
