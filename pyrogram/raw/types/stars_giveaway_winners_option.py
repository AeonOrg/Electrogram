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


class StarsGiveawayWinnersOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsGiveawayWinnersOption`.

    Details:
        - Layer: ``224``
        - ID: ``54236209``

    Parameters:
        users (``int`` ``32-bit``):
            N/A

        per_user_stars (``int`` ``64-bit``):
            N/A

        default (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["users", "per_user_stars", "default"]

    ID = 0x54236209
    QUALNAME = "types.StarsGiveawayWinnersOption"

    def __init__(self, *, users: int, per_user_stars: int, default: Optional[bool] = None) -> None:
        self.users = users  # int
        self.per_user_stars = per_user_stars  # long
        self.default = default  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsGiveawayWinnersOption":

        flags = Int.read(b)

        default = True if flags & (1 << 0) else False
        users = Int.read(b)

        per_user_stars = Long.read(b)

        return StarsGiveawayWinnersOption(users=users, per_user_stars=per_user_stars, default=default)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.default else 0
        b.write(Int(flags))

        b.write(Int(self.users))

        b.write(Long(self.per_user_stars))

        return b.getvalue()
