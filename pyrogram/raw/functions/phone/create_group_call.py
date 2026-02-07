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


class CreateGroupCall(TLObject):  # type: ignore
    """Create a group call or livestream


    Details:
        - Layer: ``224``
        - ID: ``48CDC6D8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Associate the group call or livestream to the provided group/supergroup/channel

        random_id (``int`` ``32-bit``):
            Unique client message ID required to prevent creation of duplicate group calls

        rtmp_stream (``bool``, *optional*):
            Whether RTMP stream support should be enabled: only the group/supergroup/channel owner can use this flag.

        title (``str``, *optional*):
            Call title

        schedule_date (``int`` ``32-bit``, *optional*):
            For scheduled group call or livestreams, the absolute date when the group call will start

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "rtmp_stream", "title", "schedule_date"]

    ID = 0x48cdc6d8
    QUALNAME = "functions.phone.CreateGroupCall"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, rtmp_stream: Optional[bool] = None, title: Optional[str] = None, schedule_date: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.random_id = random_id  # int
        self.rtmp_stream = rtmp_stream  # flags.2?true
        self.title = title  # flags.0?string
        self.schedule_date = schedule_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateGroupCall":

        flags = Int.read(b)

        rtmp_stream = True if flags & (1 << 2) else False
        peer = TLObject.read(b)

        random_id = Int.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        schedule_date = Int.read(b) if flags & (1 << 1) else None
        return CreateGroupCall(peer=peer, random_id=random_id, rtmp_stream=rtmp_stream, title=title, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.rtmp_stream else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.schedule_date is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.random_id))

        if self.title is not None:
            b.write(String(self.title))

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        return b.getvalue()
