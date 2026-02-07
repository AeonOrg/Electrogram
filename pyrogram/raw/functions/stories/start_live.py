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


class StartLive(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D069CCDE``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        privacy_rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        rtmp_stream (``bool``, *optional*):
            N/A

        caption (``str``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        messages_enabled (``bool``, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "privacy_rules", "random_id", "pinned", "noforwards", "rtmp_stream", "caption", "entities", "messages_enabled", "send_paid_messages_stars"]

    ID = 0xd069ccde
    QUALNAME = "functions.stories.StartLive"

    def __init__(self, *, peer: "raw.base.InputPeer", privacy_rules: List["raw.base.InputPrivacyRule"], random_id: int, pinned: Optional[bool] = None, noforwards: Optional[bool] = None, rtmp_stream: Optional[bool] = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.privacy_rules = privacy_rules  # Vector<InputPrivacyRule>
        self.random_id = random_id  # long
        self.pinned = pinned  # flags.2?true
        self.noforwards = noforwards  # flags.4?true
        self.rtmp_stream = rtmp_stream  # flags.5?true
        self.caption = caption  # flags.0?string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.messages_enabled = messages_enabled  # flags.6?Bool
        self.send_paid_messages_stars = send_paid_messages_stars  # flags.7?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartLive":

        flags = Int.read(b)

        pinned = True if flags & (1 << 2) else False
        noforwards = True if flags & (1 << 4) else False
        rtmp_stream = True if flags & (1 << 5) else False
        peer = TLObject.read(b)

        caption = String.read(b) if flags & (1 << 0) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []

        privacy_rules = TLObject.read(b)

        random_id = Long.read(b)

        messages_enabled = Bool.read(b) if flags & (1 << 6) else None
        send_paid_messages_stars = Long.read(b) if flags & (1 << 7) else None
        return StartLive(peer=peer, privacy_rules=privacy_rules, random_id=random_id, pinned=pinned, noforwards=noforwards, rtmp_stream=rtmp_stream, caption=caption, entities=entities, messages_enabled=messages_enabled, send_paid_messages_stars=send_paid_messages_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        flags |= (1 << 4) if self.noforwards else 0
        flags |= (1 << 5) if self.rtmp_stream else 0
        flags |= (1 << 0) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 6) if self.messages_enabled is not None else 0
        flags |= (1 << 7) if self.send_paid_messages_stars is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.caption is not None:
            b.write(String(self.caption))

        if self.entities is not None:
            b.write(Vector(self.entities))

        b.write(Vector(self.privacy_rules))

        b.write(Long(self.random_id))

        if self.messages_enabled is not None:
            b.write(Bool(self.messages_enabled))

        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))

        return b.getvalue()
