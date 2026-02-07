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


class GetTheme(TLObject):  # type: ignore
    """Get theme information


    Details:
        - Layer: ``224``
        - ID: ``3A5869EC``

    Parameters:
        format (``str``):
            Theme format, a string that identifies the theming engines supported by the client

        theme (:obj:`InputTheme <pyrogram.raw.base.InputTheme>`):
            Theme

    Returns:
        :obj:`Theme <pyrogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["format", "theme"]

    ID = 0x3a5869ec
    QUALNAME = "functions.account.GetTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme") -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTheme":
        # No flags

        format = String.read(b)

        theme = TLObject.read(b)

        return GetTheme(format=format, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.format))

        b.write(self.theme.write())

        return b.getvalue()
