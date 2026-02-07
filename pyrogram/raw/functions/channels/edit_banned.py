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


class EditBanned(TLObject):  # type: ignore
    """Ban/unban/kick a user in a supergroup/channel.


    Details:
        - Layer: ``224``
        - ID: ``96E6CD81``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            The supergroup/channel.

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Participant to ban

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            The banned rights

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "participant", "banned_rights"]

    ID = 0x96e6cd81
    QUALNAME = "functions.channels.EditBanned"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer", banned_rights: "raw.base.ChatBannedRights") -> None:
        self.channel = channel  # InputChannel
        self.participant = participant  # InputPeer
        self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBanned":
        # No flags

        channel = TLObject.read(b)

        participant = TLObject.read(b)

        banned_rights = TLObject.read(b)

        return EditBanned(channel=channel, participant=participant, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.participant.write())

        b.write(self.banned_rights.write())

        return b.getvalue()
