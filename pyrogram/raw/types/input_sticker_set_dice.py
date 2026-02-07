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


class InputStickerSetDice(TLObject):  # type: ignore
    """Used for fetching animated dice stickers

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``E67F520E``

    Parameters:
        emoticon (``str``):
            The emoji, for now ,  and  are supported

    """

    __slots__: List[str] = ["emoticon"]

    ID = 0xe67f520e
    QUALNAME = "types.InputStickerSetDice"

    def __init__(self, *, emoticon: str) -> None:
        self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetDice":
        # No flags

        emoticon = String.read(b)

        return InputStickerSetDice(emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.emoticon))

        return b.getvalue()
