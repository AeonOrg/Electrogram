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


class InviteToChannel(TLObject):  # type: ignore
    """Invite users to a channel/supergroup


    Details:
        - Layer: ``224``
        - ID: ``C9E33D54``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Users to invite

    Returns:
        :obj:`messages.InvitedUsers <pyrogram.raw.base.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["channel", "users"]

    ID = 0xc9e33d54
    QUALNAME = "functions.channels.InviteToChannel"

    def __init__(self, *, channel: "raw.base.InputChannel", users: List["raw.base.InputUser"]) -> None:
        self.channel = channel  # InputChannel
        self.users = users  # Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteToChannel":
        # No flags

        channel = TLObject.read(b)

        users = TLObject.read(b)

        return InviteToChannel(channel=channel, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Vector(self.users))

        return b.getvalue()
