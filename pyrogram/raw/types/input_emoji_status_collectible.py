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


class InputEmojiStatusCollectible(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiStatus`.

    Details:
        - Layer: ``224``
        - ID: ``7141DBF``

    Parameters:
        collectible_id (``int`` ``64-bit``):
            N/A

        until (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["collectible_id", "until"]

    ID = 0x7141dbf
    QUALNAME = "types.InputEmojiStatusCollectible"

    def __init__(self, *, collectible_id: int, until: Optional[int] = None) -> None:
        self.collectible_id = collectible_id  # long
        self.until = until  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEmojiStatusCollectible":

        flags = Int.read(b)

        collectible_id = Long.read(b)

        until = Int.read(b) if flags & (1 << 0) else None
        return InputEmojiStatusCollectible(collectible_id=collectible_id, until=until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.until is not None else 0
        b.write(Int(flags))

        b.write(Long(self.collectible_id))

        if self.until is not None:
            b.write(Int(self.until))

        return b.getvalue()
