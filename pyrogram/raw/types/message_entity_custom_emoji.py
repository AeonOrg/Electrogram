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


class MessageEntityCustomEmoji(TLObject):  # type: ignore
    """Represents a custom emoji.
Note that this entity must wrap exactly one regular emoji (the one contained in documentAttributeCustomEmoji.alt) in the related text, otherwise the server will ignore it.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``C8CF05F8``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset of message entity within message (in UTF-16 code units)

        length (``int`` ``32-bit``):
            Length of message entity within message (in UTF-16 code units)

        document_id (``int`` ``64-bit``):
            Document ID of the custom emoji, use messages.getCustomEmojiDocuments to fetch the emoji animation and the actual emoji it represents.

    """

    __slots__: List[str] = ["offset", "length", "document_id"]

    ID = 0xc8cf05f8
    QUALNAME = "types.MessageEntityCustomEmoji"

    def __init__(self, *, offset: int, length: int, document_id: int) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityCustomEmoji":
        # No flags

        offset = Int.read(b)

        length = Int.read(b)

        document_id = Long.read(b)

        return MessageEntityCustomEmoji(offset=offset, length=length, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.offset))

        b.write(Int(self.length))

        b.write(Long(self.document_id))

        return b.getvalue()
