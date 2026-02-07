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


class ActivateStealthMode(TLObject):  # type: ignore
    """Activates stories stealth mode, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``57BBD166``

    Parameters:
        past (``bool``, *optional*):
            Whether to erase views from any stories opened in the past stories_stealth_past_period seconds », as specified by the client configuration.

        future (``bool``, *optional*):
            Whether to hide future story views for the next stories_stealth_future_period seconds », as specified by the client configuration.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["past", "future"]

    ID = 0x57bbd166
    QUALNAME = "functions.stories.ActivateStealthMode"

    def __init__(self, *, past: Optional[bool] = None, future: Optional[bool] = None) -> None:
        self.past = past  # flags.0?true
        self.future = future  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ActivateStealthMode":

        flags = Int.read(b)

        past = True if flags & (1 << 0) else False
        future = True if flags & (1 << 1) else False
        return ActivateStealthMode(past=past, future=future)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.past else 0
        flags |= (1 << 1) if self.future else 0
        b.write(Int(flags))

        return b.getvalue()
