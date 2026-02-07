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


class EmojiGameOutcome(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGameOutcome`.

    Details:
        - Layer: ``224``
        - ID: ``DA2AD647``

    Parameters:
        seed (``bytes``):
            N/A

        stake_ton_amount (``int`` ``64-bit``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["seed", "stake_ton_amount", "ton_amount"]

    ID = 0xda2ad647
    QUALNAME = "types.messages.EmojiGameOutcome"

    def __init__(self, *, seed: bytes, stake_ton_amount: int, ton_amount: int) -> None:
        self.seed = seed  # bytes
        self.stake_ton_amount = stake_ton_amount  # long
        self.ton_amount = ton_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGameOutcome":
        # No flags

        seed = Bytes.read(b)

        stake_ton_amount = Long.read(b)

        ton_amount = Long.read(b)

        return EmojiGameOutcome(seed=seed, stake_ton_amount=stake_ton_amount, ton_amount=ton_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.seed))

        b.write(Long(self.stake_ton_amount))

        b.write(Long(self.ton_amount))

        return b.getvalue()
