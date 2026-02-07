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


class Poll(TLObject):  # type: ignore
    """Poll

    Constructor of :obj:`~pyrogram.raw.base.Poll`.

    Details:
        - Layer: ``224``
        - ID: ``58747131``

    Parameters:
        id (``int`` ``64-bit``):
            ID of the poll

        question (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            The question of the poll

        answers (List of :obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            The possible answers, vote using messages.sendVote.

        closed (``bool``, *optional*):
            Whether the poll is closed and doesn't accept any more answers

        public_voters (``bool``, *optional*):
            Whether cast votes are publicly visible to all users (non-anonymous poll)

        multiple_choice (``bool``, *optional*):
            Whether multiple options can be chosen as answer

        quiz (``bool``, *optional*):
            Whether this is a quiz (with wrong and correct answers, results shown in the return type)

        close_period (``int`` ``32-bit``, *optional*):
            Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.

        close_date (``int`` ``32-bit``, *optional*):
            Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future; can't be used together with close_period.

    """

    __slots__: List[str] = ["id", "question", "answers", "closed", "public_voters", "multiple_choice", "quiz", "close_period", "close_date"]

    ID = 0x58747131
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: "raw.base.TextWithEntities", answers: List["raw.base.PollAnswer"], closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[int] = None) -> None:
        self.id = id  # long
        self.question = question  # TextWithEntities
        self.answers = answers  # Vector<PollAnswer>
        self.closed = closed  # flags.0?true
        self.public_voters = public_voters  # flags.1?true
        self.multiple_choice = multiple_choice  # flags.2?true
        self.quiz = quiz  # flags.3?true
        self.close_period = close_period  # flags.4?int
        self.close_date = close_date  # flags.5?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Poll":

        id = Long.read(b)

        flags = Int.read(b)

        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        question = TLObject.read(b)

        answers = TLObject.read(b)

        close_period = Int.read(b) if flags & (1 << 4) else None
        close_date = Int.read(b) if flags & (1 << 5) else None
        return Poll(id=id, question=question, answers=answers, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, close_period=close_period, close_date=close_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))


        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed else 0
        flags |= (1 << 1) if self.public_voters else 0
        flags |= (1 << 2) if self.multiple_choice else 0
        flags |= (1 << 3) if self.quiz else 0
        flags |= (1 << 4) if self.close_period is not None else 0
        flags |= (1 << 5) if self.close_date is not None else 0
        b.write(Int(flags))

        b.write(self.question.write())

        b.write(Vector(self.answers))

        if self.close_period is not None:
            b.write(Int(self.close_period))

        if self.close_date is not None:
            b.write(Int(self.close_date))

        return b.getvalue()
