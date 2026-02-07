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


class EditStory(TLObject):  # type: ignore
    """Edit an uploaded story


    Details:
        - Layer: ``224``
        - ID: ``B583BA46``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the story was posted.

        id (``int`` ``32-bit``):
            ID of story to edit.

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            If specified, replaces the story media.

        media_areas (List of :obj:`MediaArea <pyrogram.raw.base.MediaArea>`, *optional*):
            Media areas associated to the story, see here » for more info.

        caption (``str``, *optional*):
            If specified, replaces the story caption.

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text in the caption, if allowed by the stories_entities client configuration parameter ».

        privacy_rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`, *optional*):
            If specified, alters the privacy settings » of the story, changing who can or can't view the story.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "media", "media_areas", "caption", "entities", "privacy_rules"]

    ID = 0xb583ba46
    QUALNAME = "functions.stories.EditStory"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, media: "raw.base.InputMedia" = None, media_areas: Optional[List["raw.base.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, privacy_rules: Optional[List["raw.base.InputPrivacyRule"]] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.media = media  # flags.0?InputMedia
        self.media_areas = media_areas  # flags.3?Vector<MediaArea>
        self.caption = caption  # flags.1?string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.privacy_rules = privacy_rules  # flags.2?Vector<InputPrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditStory":

        flags = Int.read(b)

        peer = TLObject.read(b)

        id = Int.read(b)

        media = TLObject.read(b) if flags & (1 << 0) else None

        media_areas = TLObject.read(b) if flags & (1 << 3) else []

        caption = String.read(b) if flags & (1 << 1) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []

        privacy_rules = TLObject.read(b) if flags & (1 << 2) else []

        return EditStory(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media is not None else 0
        flags |= (1 << 3) if self.media_areas else 0
        flags |= (1 << 1) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.privacy_rules else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        if self.media is not None:
            b.write(self.media.write())

        if self.media_areas is not None:
            b.write(Vector(self.media_areas))

        if self.caption is not None:
            b.write(String(self.caption))

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.privacy_rules is not None:
            b.write(Vector(self.privacy_rules))

        return b.getvalue()
