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


class UpdateServiceNotification(TLObject):  # type: ignore
    """A service message for the user.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EBE46819``

    Parameters:
        type (``str``):
            String, identical in format and contents to the type field in API errors. Describes type of service message. It is acceptable to ignore repeated messages of the same type within a short period of time (15 minutes).

        message (``str``):
            Message text

        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            Media content (optional)

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            Message entities for styled text

        popup (``bool``, *optional*):
            If set, the message must be displayed in a popup.

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        inbox_date (``int`` ``32-bit``, *optional*):
            When was the notification receivedThe message must also be stored locally as part of the message history with the user id 777000 (Telegram Notifications).

    """

    __slots__: List[str] = ["type", "message", "media", "entities", "popup", "invert_media", "inbox_date"]

    ID = 0xebe46819
    QUALNAME = "types.UpdateServiceNotification"

    def __init__(self, *, type: str, message: str, media: "raw.base.MessageMedia", entities: List["raw.base.MessageEntity"], popup: Optional[bool] = None, invert_media: Optional[bool] = None, inbox_date: Optional[int] = None) -> None:
        self.type = type  # string
        self.message = message  # string
        self.media = media  # MessageMedia
        self.entities = entities  # Vector<MessageEntity>
        self.popup = popup  # flags.0?true
        self.invert_media = invert_media  # flags.2?true
        self.inbox_date = inbox_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateServiceNotification":

        flags = Int.read(b)

        popup = True if flags & (1 << 0) else False
        invert_media = True if flags & (1 << 2) else False
        inbox_date = Int.read(b) if flags & (1 << 1) else None
        type = String.read(b)

        message = String.read(b)

        media = TLObject.read(b)

        entities = TLObject.read(b)

        return UpdateServiceNotification(type=type, message=message, media=media, entities=entities, popup=popup, invert_media=invert_media, inbox_date=inbox_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup else 0
        flags |= (1 << 2) if self.invert_media else 0
        flags |= (1 << 1) if self.inbox_date is not None else 0
        b.write(Int(flags))

        if self.inbox_date is not None:
            b.write(Int(self.inbox_date))

        b.write(String(self.type))

        b.write(String(self.message))

        b.write(self.media.write())

        b.write(Vector(self.entities))

        return b.getvalue()
