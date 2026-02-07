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


class BotAppSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotAppSettings`.

    Details:
        - Layer: ``224``
        - ID: ``C99B1950``

    Parameters:
        placeholder_path (``bytes``, *optional*):
            N/A

        background_color (``int`` ``32-bit``, *optional*):
            N/A

        background_dark_color (``int`` ``32-bit``, *optional*):
            N/A

        header_color (``int`` ``32-bit``, *optional*):
            N/A

        header_dark_color (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["placeholder_path", "background_color", "background_dark_color", "header_color", "header_dark_color"]

    ID = 0xc99b1950
    QUALNAME = "types.BotAppSettings"

    def __init__(self, *, placeholder_path: Optional[bytes] = None, background_color: Optional[int] = None, background_dark_color: Optional[int] = None, header_color: Optional[int] = None, header_dark_color: Optional[int] = None) -> None:
        self.placeholder_path = placeholder_path  # flags.0?bytes
        self.background_color = background_color  # flags.1?int
        self.background_dark_color = background_dark_color  # flags.2?int
        self.header_color = header_color  # flags.3?int
        self.header_dark_color = header_dark_color  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotAppSettings":

        flags = Int.read(b)

        placeholder_path = Bytes.read(b) if flags & (1 << 0) else None
        background_color = Int.read(b) if flags & (1 << 1) else None
        background_dark_color = Int.read(b) if flags & (1 << 2) else None
        header_color = Int.read(b) if flags & (1 << 3) else None
        header_dark_color = Int.read(b) if flags & (1 << 4) else None
        return BotAppSettings(placeholder_path=placeholder_path, background_color=background_color, background_dark_color=background_dark_color, header_color=header_color, header_dark_color=header_dark_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.placeholder_path is not None else 0
        flags |= (1 << 1) if self.background_color is not None else 0
        flags |= (1 << 2) if self.background_dark_color is not None else 0
        flags |= (1 << 3) if self.header_color is not None else 0
        flags |= (1 << 4) if self.header_dark_color is not None else 0
        b.write(Int(flags))

        if self.placeholder_path is not None:
            b.write(Bytes(self.placeholder_path))

        if self.background_color is not None:
            b.write(Int(self.background_color))

        if self.background_dark_color is not None:
            b.write(Int(self.background_dark_color))

        if self.header_color is not None:
            b.write(Int(self.header_color))

        if self.header_dark_color is not None:
            b.write(Int(self.header_dark_color))

        return b.getvalue()
