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


class PollAnswerVoters(TLObject):  # type: ignore
    """A poll answer, and how users voted on it

    Constructor of :obj:`~pyrogram.raw.base.PollAnswerVoters`.

    Details:
        - Layer: ``224``
        - ID: ``3B6DDAD2``

    Parameters:
        option (``bytes``):
            The param that has to be passed to messages.sendVote.

        voters (``int`` ``32-bit``):
            How many users voted for this option

        chosen (``bool``, *optional*):
            Whether we have chosen this answer

        correct (``bool``, *optional*):
            For quizzes, whether the option we have chosen is correct

    """

    __slots__: List[str] = ["option", "voters", "chosen", "correct"]

    ID = 0x3b6ddad2
    QUALNAME = "types.PollAnswerVoters"

    def __init__(self, *, option: bytes, voters: int, chosen: Optional[bool] = None, correct: Optional[bool] = None) -> None:
        self.option = option  # bytes
        self.voters = voters  # int
        self.chosen = chosen  # flags.0?true
        self.correct = correct  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswerVoters":

        flags = Int.read(b)

        chosen = True if flags & (1 << 0) else False
        correct = True if flags & (1 << 1) else False
        option = Bytes.read(b)

        voters = Int.read(b)

        return PollAnswerVoters(option=option, voters=voters, chosen=chosen, correct=correct)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen else 0
        flags |= (1 << 1) if self.correct else 0
        b.write(Int(flags))

        b.write(Bytes(self.option))

        b.write(Int(self.voters))

        return b.getvalue()
