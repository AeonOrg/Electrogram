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


class EditGroupCallParticipant(TLObject):  # type: ignore
    """Edit information about a given group call participant


    Details:
        - Layer: ``224``
        - ID: ``A5273ABF``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            The group call

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The group call participant (can also be the user itself)

        muted (``bool``, *optional*):
            Whether to mute or unmute the specified participant

        volume (``int`` ``32-bit``, *optional*):
            New volume

        raise_hand (``bool``, *optional*):
            Raise or lower hand

        video_stopped (``bool``, *optional*):
            Start or stop the video stream

        video_paused (``bool``, *optional*):
            Pause or resume the video stream

        presentation_paused (``bool``, *optional*):
            Pause or resume the screen sharing stream

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "muted", "volume", "raise_hand", "video_stopped", "video_paused", "presentation_paused"]

    ID = 0xa5273abf
    QUALNAME = "functions.phone.EditGroupCallParticipant"

    def __init__(self, *, call: "raw.base.InputGroupCall", participant: "raw.base.InputPeer", muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.muted = muted  # flags.0?Bool
        self.volume = volume  # flags.1?int
        self.raise_hand = raise_hand  # flags.2?Bool
        self.video_stopped = video_stopped  # flags.3?Bool
        self.video_paused = video_paused  # flags.4?Bool
        self.presentation_paused = presentation_paused  # flags.5?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditGroupCallParticipant":

        flags = Int.read(b)

        call = TLObject.read(b)

        participant = TLObject.read(b)

        muted = Bool.read(b) if flags & (1 << 0) else None
        volume = Int.read(b) if flags & (1 << 1) else None
        raise_hand = Bool.read(b) if flags & (1 << 2) else None
        video_stopped = Bool.read(b) if flags & (1 << 3) else None
        video_paused = Bool.read(b) if flags & (1 << 4) else None
        presentation_paused = Bool.read(b) if flags & (1 << 5) else None
        return EditGroupCallParticipant(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand, video_stopped=video_stopped, video_paused=video_paused, presentation_paused=presentation_paused)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted is not None else 0
        flags |= (1 << 1) if self.volume is not None else 0
        flags |= (1 << 2) if self.raise_hand is not None else 0
        flags |= (1 << 3) if self.video_stopped is not None else 0
        flags |= (1 << 4) if self.video_paused is not None else 0
        flags |= (1 << 5) if self.presentation_paused is not None else 0
        b.write(Int(flags))

        b.write(self.call.write())

        b.write(self.participant.write())

        if self.muted is not None:
            b.write(Bool(self.muted))

        if self.volume is not None:
            b.write(Int(self.volume))

        if self.raise_hand is not None:
            b.write(Bool(self.raise_hand))

        if self.video_stopped is not None:
            b.write(Bool(self.video_stopped))

        if self.video_paused is not None:
            b.write(Bool(self.video_paused))

        if self.presentation_paused is not None:
            b.write(Bool(self.presentation_paused))

        return b.getvalue()
