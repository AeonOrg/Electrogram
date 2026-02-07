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


class MessageActionConferenceCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``2FFE2F7A``

    Parameters:
        call_id (``int`` ``64-bit``):
            N/A

        missed (``bool``, *optional*):
            N/A

        active (``bool``, *optional*):
            N/A

        video (``bool``, *optional*):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

        other_participants (List of :obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["call_id", "missed", "active", "video", "duration", "other_participants"]

    ID = 0x2ffe2f7a
    QUALNAME = "types.MessageActionConferenceCall"

    def __init__(self, *, call_id: int, missed: Optional[bool] = None, active: Optional[bool] = None, video: Optional[bool] = None, duration: Optional[int] = None, other_participants: Optional[List["raw.base.Peer"]] = None) -> None:
        self.call_id = call_id  # long
        self.missed = missed  # flags.0?true
        self.active = active  # flags.1?true
        self.video = video  # flags.4?true
        self.duration = duration  # flags.2?int
        self.other_participants = other_participants  # flags.3?Vector<Peer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionConferenceCall":

        flags = Int.read(b)

        missed = True if flags & (1 << 0) else False
        active = True if flags & (1 << 1) else False
        video = True if flags & (1 << 4) else False
        call_id = Long.read(b)

        duration = Int.read(b) if flags & (1 << 2) else None
        other_participants = TLObject.read(b) if flags & (1 << 3) else []

        return MessageActionConferenceCall(call_id=call_id, missed=missed, active=active, video=video, duration=duration, other_participants=other_participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missed else 0
        flags |= (1 << 1) if self.active else 0
        flags |= (1 << 4) if self.video else 0
        flags |= (1 << 2) if self.duration is not None else 0
        flags |= (1 << 3) if self.other_participants else 0
        b.write(Int(flags))

        b.write(Long(self.call_id))

        if self.duration is not None:
            b.write(Int(self.duration))

        if self.other_participants is not None:
            b.write(Vector(self.other_participants))

        return b.getvalue()
