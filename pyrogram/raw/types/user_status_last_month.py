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


class UserStatusLastMonth(TLObject):  # type: ignore
    """Online status: last seen last month

    Constructor of :obj:`~pyrogram.raw.base.UserStatus`.

    Details:
        - Layer: ``224``
        - ID: ``65899777``

    Parameters:
        by_me (``bool``, *optional*):


    """

    __slots__: List[str] = ["by_me"]

    ID = 0x65899777
    QUALNAME = "types.UserStatusLastMonth"

    def __init__(self, *, by_me: Optional[bool] = None) -> None:
        self.by_me = by_me  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusLastMonth":

        flags = Int.read(b)

        by_me = True if flags & (1 << 0) else False
        return UserStatusLastMonth(by_me=by_me)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_me else 0
        b.write(Int(flags))

        return b.getvalue()
