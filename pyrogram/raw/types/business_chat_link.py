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


class BusinessChatLink(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessChatLink`.

    Details:
        - Layer: ``224``
        - ID: ``B4AE666F``

    Parameters:
        link (``str``):


        message (``str``):


        views (``int`` ``32-bit``):


        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        title (``str``, *optional*):


    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.CreateBusinessChatLink
            account.EditBusinessChatLink
    """

    __slots__: List[str] = ["link", "message", "views", "entities", "title"]

    ID = 0xb4ae666f
    QUALNAME = "types.BusinessChatLink"

    def __init__(self, *, link: str, message: str, views: int, entities: Optional[List["raw.base.MessageEntity"]] = None, title: Optional[str] = None) -> None:
        self.link = link  # string
        self.message = message  # string
        self.views = views  # int
        self.entities = entities  # flags.0?Vector<MessageEntity>
        self.title = title  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessChatLink":

        flags = Int.read(b)

        link = String.read(b)

        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 0) else []

        title = String.read(b) if flags & (1 << 1) else None
        views = Int.read(b)

        return BusinessChatLink(link=link, message=message, views=views, entities=entities, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.entities else 0
        flags |= (1 << 1) if self.title is not None else 0
        b.write(Int(flags))

        b.write(String(self.link))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.title is not None:
            b.write(String(self.title))

        b.write(Int(self.views))

        return b.getvalue()
