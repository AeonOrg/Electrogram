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


class ResolveBusinessChatLink(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``5492E5EE``

    Parameters:
        slug (``str``):


    Returns:
        :obj:`account.ResolvedBusinessChatLinks <pyrogram.raw.base.account.ResolvedBusinessChatLinks>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x5492e5ee
    QUALNAME = "functions.account.ResolveBusinessChatLink"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveBusinessChatLink":
        # No flags

        slug = String.read(b)

        return ResolveBusinessChatLink(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
