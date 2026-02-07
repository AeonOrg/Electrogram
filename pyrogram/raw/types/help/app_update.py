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


class AppUpdate(TLObject):  # type: ignore
    """An update is available for the application.

    Constructor of :obj:`~pyrogram.raw.base.help.AppUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``CCBBCE30``

    Parameters:
        id (``int`` ``32-bit``):
            Update ID

        version (``str``):
            New version name

        text (``str``):
            Text description of the update

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            Message entities for styled text

        can_not_skip (``bool``, *optional*):
            Unskippable, the new info must be shown to the user (with a popup or something else)

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            Application binary

        url (``str``, *optional*):
            Application download URL

        sticker (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            Associated sticker

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppUpdate
    """

    __slots__: List[str] = ["id", "version", "text", "entities", "can_not_skip", "document", "url", "sticker"]

    ID = 0xccbbce30
    QUALNAME = "types.help.AppUpdate"

    def __init__(self, *, id: int, version: str, text: str, entities: List["raw.base.MessageEntity"], can_not_skip: Optional[bool] = None, document: "raw.base.Document" = None, url: Optional[str] = None, sticker: "raw.base.Document" = None) -> None:
        self.id = id  # int
        self.version = version  # string
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.can_not_skip = can_not_skip  # flags.0?true
        self.document = document  # flags.1?Document
        self.url = url  # flags.2?string
        self.sticker = sticker  # flags.3?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppUpdate":

        flags = Int.read(b)

        can_not_skip = True if flags & (1 << 0) else False
        id = Int.read(b)

        version = String.read(b)

        text = String.read(b)

        entities = TLObject.read(b)

        document = TLObject.read(b) if flags & (1 << 1) else None

        url = String.read(b) if flags & (1 << 2) else None
        sticker = TLObject.read(b) if flags & (1 << 3) else None

        return AppUpdate(id=id, version=version, text=text, entities=entities, can_not_skip=can_not_skip, document=document, url=url, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_not_skip else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        flags |= (1 << 3) if self.sticker is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(String(self.version))

        b.write(String(self.text))

        b.write(Vector(self.entities))

        if self.document is not None:
            b.write(self.document.write())

        if self.url is not None:
            b.write(String(self.url))

        if self.sticker is not None:
            b.write(self.sticker.write())

        return b.getvalue()
