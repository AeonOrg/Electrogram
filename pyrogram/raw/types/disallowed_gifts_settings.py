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


class DisallowedGiftsSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DisallowedGiftsSettings`.

    Details:
        - Layer: ``224``
        - ID: ``71F276C4``

    Parameters:
        disallow_unlimited_stargifts (``bool``, *optional*):
            N/A

        disallow_limited_stargifts (``bool``, *optional*):
            N/A

        disallow_unique_stargifts (``bool``, *optional*):
            N/A

        disallow_premium_gifts (``bool``, *optional*):
            N/A

        disallow_stargifts_from_channels (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["disallow_unlimited_stargifts", "disallow_limited_stargifts", "disallow_unique_stargifts", "disallow_premium_gifts", "disallow_stargifts_from_channels"]

    ID = 0x71f276c4
    QUALNAME = "types.DisallowedGiftsSettings"

    def __init__(self, *, disallow_unlimited_stargifts: Optional[bool] = None, disallow_limited_stargifts: Optional[bool] = None, disallow_unique_stargifts: Optional[bool] = None, disallow_premium_gifts: Optional[bool] = None, disallow_stargifts_from_channels: Optional[bool] = None) -> None:
        self.disallow_unlimited_stargifts = disallow_unlimited_stargifts  # flags.0?true
        self.disallow_limited_stargifts = disallow_limited_stargifts  # flags.1?true
        self.disallow_unique_stargifts = disallow_unique_stargifts  # flags.2?true
        self.disallow_premium_gifts = disallow_premium_gifts  # flags.3?true
        self.disallow_stargifts_from_channels = disallow_stargifts_from_channels  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DisallowedGiftsSettings":

        flags = Int.read(b)

        disallow_unlimited_stargifts = True if flags & (1 << 0) else False
        disallow_limited_stargifts = True if flags & (1 << 1) else False
        disallow_unique_stargifts = True if flags & (1 << 2) else False
        disallow_premium_gifts = True if flags & (1 << 3) else False
        disallow_stargifts_from_channels = True if flags & (1 << 4) else False
        return DisallowedGiftsSettings(disallow_unlimited_stargifts=disallow_unlimited_stargifts, disallow_limited_stargifts=disallow_limited_stargifts, disallow_unique_stargifts=disallow_unique_stargifts, disallow_premium_gifts=disallow_premium_gifts, disallow_stargifts_from_channels=disallow_stargifts_from_channels)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.disallow_unlimited_stargifts else 0
        flags |= (1 << 1) if self.disallow_limited_stargifts else 0
        flags |= (1 << 2) if self.disallow_unique_stargifts else 0
        flags |= (1 << 3) if self.disallow_premium_gifts else 0
        flags |= (1 << 4) if self.disallow_stargifts_from_channels else 0
        b.write(Int(flags))

        return b.getvalue()
