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


class GetSavedMusic(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``788D7FE3``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`users.SavedMusic <pyrogram.raw.base.users.SavedMusic>`
    """

    __slots__: List[str] = ["id", "offset", "limit", "hash"]

    ID = 0x788d7fe3
    QUALNAME = "functions.users.GetSavedMusic"

    def __init__(self, *, id: "raw.base.InputUser", offset: int, limit: int, hash: int) -> None:
        self.id = id  # InputUser
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedMusic":
        # No flags

        id = TLObject.read(b)

        offset = Int.read(b)

        limit = Int.read(b)

        hash = Long.read(b)

        return GetSavedMusic(id=id, offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.id.write())

        b.write(Int(self.offset))

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
