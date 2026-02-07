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


class PollAnswer(TLObject):  # type: ignore
    """A possible answer of a poll

    Constructor of :obj:`~pyrogram.raw.base.PollAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``FF16E2CA``

    Parameters:
        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            Textual representation of the answer

        option (``bytes``):
            The param that has to be passed to messages.sendVote.

    """

    __slots__: List[str] = ["text", "option"]

    ID = 0xff16e2ca
    QUALNAME = "types.PollAnswer"

    def __init__(self, *, text: "raw.base.TextWithEntities", option: bytes) -> None:
        self.text = text  # TextWithEntities
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswer":
        # No flags

        text = TLObject.read(b)

        option = Bytes.read(b)

        return PollAnswer(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        b.write(Bytes(self.option))

        return b.getvalue()
