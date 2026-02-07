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


class EmojiGameDiceInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGameInfo`.

    Details:
        - Layer: ``224``
        - ID: ``44E56023``

    Parameters:
        game_hash (``str``):
            N/A

        prev_stake (``int`` ``64-bit``):
            N/A

        current_streak (``int`` ``32-bit``):
            N/A

        params (List of ``int`` ``32-bit``):
            N/A

        plays_left (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGameInfo
    """

    __slots__: List[str] = ["game_hash", "prev_stake", "current_streak", "params", "plays_left"]

    ID = 0x44e56023
    QUALNAME = "types.messages.EmojiGameDiceInfo"

    def __init__(self, *, game_hash: str, prev_stake: int, current_streak: int, params: List[int], plays_left: Optional[int] = None) -> None:
        self.game_hash = game_hash  # string
        self.prev_stake = prev_stake  # long
        self.current_streak = current_streak  # int
        self.params = params  # Vector<int>
        self.plays_left = plays_left  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGameDiceInfo":

        flags = Int.read(b)

        game_hash = String.read(b)

        prev_stake = Long.read(b)

        current_streak = Int.read(b)

        params = TLObject.read(b, Int)

        plays_left = Int.read(b) if flags & (1 << 0) else None
        return EmojiGameDiceInfo(game_hash=game_hash, prev_stake=prev_stake, current_streak=current_streak, params=params, plays_left=plays_left)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.plays_left is not None else 0
        b.write(Int(flags))

        b.write(String(self.game_hash))

        b.write(Long(self.prev_stake))

        b.write(Int(self.current_streak))

        b.write(Vector(self.params, Int))

        if self.plays_left is not None:
            b.write(Int(self.plays_left))

        return b.getvalue()
