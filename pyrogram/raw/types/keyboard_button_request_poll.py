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


class KeyboardButtonRequestPoll(TLObject):  # type: ignore
    """A button that allows the user to create and send a poll when pressed; available only in private

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``7A11D782``

    Parameters:
        text (``str``):
            Button text

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

        quiz (``bool``, *optional*):
            If set, only quiz polls can be sent

    """

    __slots__: List[str] = ["text", "style", "quiz"]

    ID = 0x7a11d782
    QUALNAME = "types.KeyboardButtonRequestPoll"

    def __init__(self, *, text: str, style: "raw.base.KeyboardButtonStyle" = None, quiz: Optional[bool] = None) -> None:
        self.text = text  # string
        self.style = style  # flags.10?KeyboardButtonStyle
        self.quiz = quiz  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPoll":

        flags = Int.read(b)

        style = TLObject.read(b) if flags & (1 << 10) else None

        quiz = Bool.read(b) if flags & (1 << 0) else None
        text = String.read(b)

        return KeyboardButtonRequestPoll(text=text, style=style, quiz=quiz)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 0) if self.quiz is not None else 0
        b.write(Int(flags))

        if self.style is not None:
            b.write(self.style.write())

        if self.quiz is not None:
            b.write(Bool(self.quiz))

        b.write(String(self.text))

        return b.getvalue()
