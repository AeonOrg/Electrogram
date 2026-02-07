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


class EmojiList(TLObject):  # type: ignore
    """Represents a list of custom emojis.

    Constructor of :obj:`~pyrogram.raw.base.EmojiList`.

    Details:
        - Layer: ``224``
        - ID: ``7A1E11D1``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        document_id (List of ``int`` ``64-bit``):
            Custom emoji IDs

    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetDefaultProfilePhotoEmojis
            account.GetDefaultGroupPhotoEmojis
            account.GetDefaultBackgroundEmojis
            account.GetChannelRestrictedStatusEmojis
            messages.SearchCustomEmoji
    """

    __slots__: List[str] = ["hash", "document_id"]

    ID = 0x7a1e11d1
    QUALNAME = "types.EmojiList"

    def __init__(self, *, hash: int, document_id: List[int]) -> None:
        self.hash = hash  # long
        self.document_id = document_id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiList":
        # No flags

        hash = Long.read(b)

        document_id = TLObject.read(b, Long)

        return EmojiList(hash=hash, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.document_id, Long))

        return b.getvalue()
