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


class SponsoredMessage(TLObject):  # type: ignore
    """A sponsored message.

    Constructor of :obj:`~pyrogram.raw.base.SponsoredMessage`.

    Details:
        - Layer: ``224``
        - ID: ``7DBF8673``

    Parameters:
        random_id (``bytes``):
            Message ID

        url (``str``):


        title (``str``):


        message (``str``):
            Sponsored message

        button_text (``str``):
            Text of the sponsored message button.

        recommended (``bool``, *optional*):
            Whether the message needs to be labeled as "recommended" instead of "sponsored"

        can_report (``bool``, *optional*):


        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):


        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

        color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):


        sponsor_info (``str``, *optional*):
            If set, contains additional information about the sponsor to be shown along with the message.

        additional_info (``str``, *optional*):
            If set, contains additional information about the sponsored message to be shown along with the message.

        min_display_duration (``int`` ``32-bit``, *optional*):
            N/A

        max_display_duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["random_id", "url", "title", "message", "button_text", "recommended", "can_report", "entities", "photo", "media", "color", "sponsor_info", "additional_info", "min_display_duration", "max_display_duration"]

    ID = 0x7dbf8673
    QUALNAME = "types.SponsoredMessage"

    def __init__(self, *, random_id: bytes, url: str, title: str, message: str, button_text: str, recommended: Optional[bool] = None, can_report: Optional[bool] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, photo: "raw.base.Photo" = None, media: "raw.base.MessageMedia" = None, color: "raw.base.PeerColor" = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None, min_display_duration: Optional[int] = None, max_display_duration: Optional[int] = None) -> None:
        self.random_id = random_id  # bytes
        self.url = url  # string
        self.title = title  # string
        self.message = message  # string
        self.button_text = button_text  # string
        self.recommended = recommended  # flags.5?true
        self.can_report = can_report  # flags.12?true
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.photo = photo  # flags.6?Photo
        self.media = media  # flags.14?MessageMedia
        self.color = color  # flags.13?PeerColor
        self.sponsor_info = sponsor_info  # flags.7?string
        self.additional_info = additional_info  # flags.8?string
        self.min_display_duration = min_display_duration  # flags.15?int
        self.max_display_duration = max_display_duration  # flags.15?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessage":

        flags = Int.read(b)

        recommended = True if flags & (1 << 5) else False
        can_report = True if flags & (1 << 12) else False
        random_id = Bytes.read(b)

        url = String.read(b)

        title = String.read(b)

        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 1) else []

        photo = TLObject.read(b) if flags & (1 << 6) else None

        media = TLObject.read(b) if flags & (1 << 14) else None

        color = TLObject.read(b) if flags & (1 << 13) else None

        button_text = String.read(b)

        sponsor_info = String.read(b) if flags & (1 << 7) else None
        additional_info = String.read(b) if flags & (1 << 8) else None
        min_display_duration = Int.read(b) if flags & (1 << 15) else None
        max_display_duration = Int.read(b) if flags & (1 << 15) else None
        return SponsoredMessage(random_id=random_id, url=url, title=title, message=message, button_text=button_text, recommended=recommended, can_report=can_report, entities=entities, photo=photo, media=media, color=color, sponsor_info=sponsor_info, additional_info=additional_info, min_display_duration=min_display_duration, max_display_duration=max_display_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.recommended else 0
        flags |= (1 << 12) if self.can_report else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 6) if self.photo is not None else 0
        flags |= (1 << 14) if self.media is not None else 0
        flags |= (1 << 13) if self.color is not None else 0
        flags |= (1 << 7) if self.sponsor_info is not None else 0
        flags |= (1 << 8) if self.additional_info is not None else 0
        flags |= (1 << 15) if self.min_display_duration is not None else 0
        flags |= (1 << 15) if self.max_display_duration is not None else 0
        b.write(Int(flags))

        b.write(Bytes(self.random_id))

        b.write(String(self.url))

        b.write(String(self.title))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.photo is not None:
            b.write(self.photo.write())

        if self.media is not None:
            b.write(self.media.write())

        if self.color is not None:
            b.write(self.color.write())

        b.write(String(self.button_text))

        if self.sponsor_info is not None:
            b.write(String(self.sponsor_info))

        if self.additional_info is not None:
            b.write(String(self.additional_info))

        if self.min_display_duration is not None:
            b.write(Int(self.min_display_duration))

        if self.max_display_duration is not None:
            b.write(Int(self.max_display_duration))

        return b.getvalue()
