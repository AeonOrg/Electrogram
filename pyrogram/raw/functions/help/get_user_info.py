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


class GetUserInfo(TLObject):  # type: ignore
    """Can only be used by TSF members to obtain internal information.


    Details:
        - Layer: ``224``
        - ID: ``38A08D3``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID

    Returns:
        :obj:`help.UserInfo <pyrogram.raw.base.help.UserInfo>`
    """

    __slots__: List[str] = ["user_id"]

    ID = 0x38a08d3
    QUALNAME = "functions.help.GetUserInfo"

    def __init__(self, *, user_id: "raw.base.InputUser") -> None:
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserInfo":
        # No flags

        user_id = TLObject.read(b)

        return GetUserInfo(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        return b.getvalue()
