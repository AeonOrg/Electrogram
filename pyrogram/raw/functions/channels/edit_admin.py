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


class EditAdmin(TLObject):  # type: ignore
    """Modify the admin rights of a user in a supergroup/channel.


    Details:
        - Layer: ``224``
        - ID: ``D33C8902``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            The supergroup/channel.

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The ID of the user whose admin rights should be modified

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`):
            The admin rights

        rank (``str``):
            Indicates the role (rank) of the admin in the group: just an arbitrary string

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "user_id", "admin_rights", "rank"]

    ID = 0xd33c8902
    QUALNAME = "functions.channels.EditAdmin"

    def __init__(self, *, channel: "raw.base.InputChannel", user_id: "raw.base.InputUser", admin_rights: "raw.base.ChatAdminRights", rank: str) -> None:
        self.channel = channel  # InputChannel
        self.user_id = user_id  # InputUser
        self.admin_rights = admin_rights  # ChatAdminRights
        self.rank = rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditAdmin":
        # No flags

        channel = TLObject.read(b)

        user_id = TLObject.read(b)

        admin_rights = TLObject.read(b)

        rank = String.read(b)

        return EditAdmin(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.user_id.write())

        b.write(self.admin_rights.write())

        b.write(String(self.rank))

        return b.getvalue()
