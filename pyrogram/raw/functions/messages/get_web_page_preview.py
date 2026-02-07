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


class GetWebPagePreview(TLObject):  # type: ignore
    """Get preview of webpage


    Details:
        - Layer: ``224``
        - ID: ``570D6F6F``

    Parameters:
        message (``str``):
            Message from which to extract the preview

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

    Returns:
        :obj:`messages.WebPagePreview <pyrogram.raw.base.messages.WebPagePreview>`
    """

    __slots__: List[str] = ["message", "entities"]

    ID = 0x570d6f6f
    QUALNAME = "functions.messages.GetWebPagePreview"

    def __init__(self, *, message: str, entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.message = message  # string
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebPagePreview":

        flags = Int.read(b)

        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 3) else []

        return GetWebPagePreview(message=message, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.entities else 0
        b.write(Int(flags))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        return b.getvalue()
