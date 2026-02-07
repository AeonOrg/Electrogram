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


class GetUniqueGiftChatThemes(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E42CE9C9``

    Parameters:
        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.ChatThemes <pyrogram.raw.base.account.ChatThemes>`
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0xe42ce9c9
    QUALNAME = "functions.account.GetUniqueGiftChatThemes"

    def __init__(self, *, offset: str, limit: int, hash: int) -> None:
        self.offset = offset  # string
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueGiftChatThemes":
        # No flags

        offset = String.read(b)

        limit = Int.read(b)

        hash = Long.read(b)

        return GetUniqueGiftChatThemes(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.offset))

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
