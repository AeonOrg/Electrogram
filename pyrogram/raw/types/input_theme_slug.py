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


class InputThemeSlug(TLObject):  # type: ignore
    """Theme by theme ID

    Constructor of :obj:`~pyrogram.raw.base.InputTheme`.

    Details:
        - Layer: ``224``
        - ID: ``F5890DF1``

    Parameters:
        slug (``str``):
            Unique theme ID obtained from a theme deep link »

    """

    __slots__: List[str] = ["slug"]

    ID = 0xf5890df1
    QUALNAME = "types.InputThemeSlug"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputThemeSlug":
        # No flags

        slug = String.read(b)

        return InputThemeSlug(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
