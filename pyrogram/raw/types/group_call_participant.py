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


class GroupCallParticipant(TLObject):  # type: ignore
    """Info about a group call participant

    Constructor of :obj:`~pyrogram.raw.base.GroupCallParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``2A3DC7AC``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer information

        date (``int`` ``32-bit``):
            When did this participant join the group call

        source (``int`` ``32-bit``):
            Source ID

        muted (``bool``, *optional*):
            Whether the participant is muted

        left (``bool``, *optional*):
            Whether the participant has left

        can_self_unmute (``bool``, *optional*):
            Whether the participant can unmute themselves

        just_joined (``bool``, *optional*):
            Whether the participant has just joined

        versioned (``bool``, *optional*):
            If set, and updateGroupCallParticipants.version < locally stored call.version, info about this participant should be ignored. If (...), and updateGroupCallParticipants.version > call.version+1, the participant list should be refetched using phone.getGroupParticipants.

        min (``bool``, *optional*):
            If not set, the volume and muted_by_you fields can be safely used to overwrite locally cached information; otherwise, volume will contain valid information only if volume_by_admin is set both in the cache and in the received constructor.

        muted_by_you (``bool``, *optional*):
            Whether this participant was muted by the current user

        volume_by_admin (``bool``, *optional*):
            Whether our volume can only changed by an admin

        is_self (``bool``, *optional*):
            N/A

        video_joined (``bool``, *optional*):
            Whether this participant is currently broadcasting video

        active_date (``int`` ``32-bit``, *optional*):
            When was this participant last active in the group call

        volume (``int`` ``32-bit``, *optional*):
            Volume, if not set the volume is set to 100%.

        about (``str``, *optional*):
            Info about this participant

        raise_hand_rating (``int`` ``64-bit``, *optional*):
            Specifies the UI visualization order of peers with raised hands: peers with a higher rating should be showed first in the list.

        video (:obj:`GroupCallParticipantVideo <pyrogram.raw.base.GroupCallParticipantVideo>`, *optional*):
            Info about the video stream the participant is currently broadcasting

        presentation (:obj:`GroupCallParticipantVideo <pyrogram.raw.base.GroupCallParticipantVideo>`, *optional*):
            Info about the screen sharing stream the participant is currently broadcasting

        paid_stars_total (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "date", "source", "muted", "left", "can_self_unmute", "just_joined", "versioned", "min", "muted_by_you", "volume_by_admin", "is_self", "video_joined", "active_date", "volume", "about", "raise_hand_rating", "video", "presentation", "paid_stars_total"]

    ID = 0x2a3dc7ac
    QUALNAME = "types.GroupCallParticipant"

    def __init__(self, *, peer: "raw.base.Peer", date: int, source: int, muted: Optional[bool] = None, left: Optional[bool] = None, can_self_unmute: Optional[bool] = None, just_joined: Optional[bool] = None, versioned: Optional[bool] = None, min: Optional[bool] = None, muted_by_you: Optional[bool] = None, volume_by_admin: Optional[bool] = None, is_self: Optional[bool] = None, video_joined: Optional[bool] = None, active_date: Optional[int] = None, volume: Optional[int] = None, about: Optional[str] = None, raise_hand_rating: Optional[int] = None, video: "raw.base.GroupCallParticipantVideo" = None, presentation: "raw.base.GroupCallParticipantVideo" = None, paid_stars_total: Optional[int] = None) -> None:
        self.peer = peer  # Peer
        self.date = date  # int
        self.source = source  # int
        self.muted = muted  # flags.0?true
        self.left = left  # flags.1?true
        self.can_self_unmute = can_self_unmute  # flags.2?true
        self.just_joined = just_joined  # flags.4?true
        self.versioned = versioned  # flags.5?true
        self.min = min  # flags.8?true
        self.muted_by_you = muted_by_you  # flags.9?true
        self.volume_by_admin = volume_by_admin  # flags.10?true
        self.is_self = is_self  # flags.12?true
        self.video_joined = video_joined  # flags.15?true
        self.active_date = active_date  # flags.3?int
        self.volume = volume  # flags.7?int
        self.about = about  # flags.11?string
        self.raise_hand_rating = raise_hand_rating  # flags.13?long
        self.video = video  # flags.6?GroupCallParticipantVideo
        self.presentation = presentation  # flags.14?GroupCallParticipantVideo
        self.paid_stars_total = paid_stars_total  # flags.16?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipant":

        flags = Int.read(b)

        muted = True if flags & (1 << 0) else False
        left = True if flags & (1 << 1) else False
        can_self_unmute = True if flags & (1 << 2) else False
        just_joined = True if flags & (1 << 4) else False
        versioned = True if flags & (1 << 5) else False
        min = True if flags & (1 << 8) else False
        muted_by_you = True if flags & (1 << 9) else False
        volume_by_admin = True if flags & (1 << 10) else False
        is_self = True if flags & (1 << 12) else False
        video_joined = True if flags & (1 << 15) else False
        peer = TLObject.read(b)

        date = Int.read(b)

        active_date = Int.read(b) if flags & (1 << 3) else None
        source = Int.read(b)

        volume = Int.read(b) if flags & (1 << 7) else None
        about = String.read(b) if flags & (1 << 11) else None
        raise_hand_rating = Long.read(b) if flags & (1 << 13) else None
        video = TLObject.read(b) if flags & (1 << 6) else None

        presentation = TLObject.read(b) if flags & (1 << 14) else None

        paid_stars_total = Long.read(b) if flags & (1 << 16) else None
        return GroupCallParticipant(peer=peer, date=date, source=source, muted=muted, left=left, can_self_unmute=can_self_unmute, just_joined=just_joined, versioned=versioned, min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin, is_self=is_self, video_joined=video_joined, active_date=active_date, volume=volume, about=about, raise_hand_rating=raise_hand_rating, video=video, presentation=presentation, paid_stars_total=paid_stars_total)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.left else 0
        flags |= (1 << 2) if self.can_self_unmute else 0
        flags |= (1 << 4) if self.just_joined else 0
        flags |= (1 << 5) if self.versioned else 0
        flags |= (1 << 8) if self.min else 0
        flags |= (1 << 9) if self.muted_by_you else 0
        flags |= (1 << 10) if self.volume_by_admin else 0
        flags |= (1 << 12) if self.is_self else 0
        flags |= (1 << 15) if self.video_joined else 0
        flags |= (1 << 3) if self.active_date is not None else 0
        flags |= (1 << 7) if self.volume is not None else 0
        flags |= (1 << 11) if self.about is not None else 0
        flags |= (1 << 13) if self.raise_hand_rating is not None else 0
        flags |= (1 << 6) if self.video is not None else 0
        flags |= (1 << 14) if self.presentation is not None else 0
        flags |= (1 << 16) if self.paid_stars_total is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.date))

        if self.active_date is not None:
            b.write(Int(self.active_date))

        b.write(Int(self.source))

        if self.volume is not None:
            b.write(Int(self.volume))

        if self.about is not None:
            b.write(String(self.about))

        if self.raise_hand_rating is not None:
            b.write(Long(self.raise_hand_rating))

        if self.video is not None:
            b.write(self.video.write())

        if self.presentation is not None:
            b.write(self.presentation.write())

        if self.paid_stars_total is not None:
            b.write(Long(self.paid_stars_total))

        return b.getvalue()
