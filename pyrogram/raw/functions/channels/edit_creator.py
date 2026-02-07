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


class EditCreator(TLObject):  # type: ignore
    """Transfer channel ownership


    Details:
        - Layer: ``224``
        - ID: ``8F38CD1F``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            New channel owner

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            2FA password of account

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "user_id", "password"]

    ID = 0x8f38cd1f
    QUALNAME = "functions.channels.EditCreator"

    def __init__(self, *, channel: "raw.base.InputChannel", user_id: "raw.base.InputUser", password: "raw.base.InputCheckPasswordSRP") -> None:
        self.channel = channel  # InputChannel
        self.user_id = user_id  # InputUser
        self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCreator":
        # No flags

        channel = TLObject.read(b)

        user_id = TLObject.read(b)

        password = TLObject.read(b)

        return EditCreator(channel=channel, user_id=user_id, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.user_id.write())

        b.write(self.password.write())

        return b.getvalue()
