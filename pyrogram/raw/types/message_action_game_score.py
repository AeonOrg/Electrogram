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


class MessageActionGameScore(TLObject):  # type: ignore
    """Someone scored in a game

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``92A72876``

    Parameters:
        game_id (``int`` ``64-bit``):
            Game ID

        score (``int`` ``32-bit``):
            Score

    """

    __slots__: List[str] = ["game_id", "score"]

    ID = 0x92a72876
    QUALNAME = "types.MessageActionGameScore"

    def __init__(self, *, game_id: int, score: int) -> None:
        self.game_id = game_id  # long
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGameScore":
        # No flags

        game_id = Long.read(b)

        score = Int.read(b)

        return MessageActionGameScore(game_id=game_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.game_id))

        b.write(Int(self.score))

        return b.getvalue()
