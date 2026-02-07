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


class ToggleGroupCallSettings(TLObject):  # type: ignore
    """Change group call settings


    Details:
        - Layer: ``224``
        - ID: ``974392F2``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

        reset_invite_hash (``bool``, *optional*):
            Invalidate existing invite links

        join_muted (``bool``, *optional*):
            Whether all users will that join this group call are muted by default upon joining the group call

        messages_enabled (``bool``, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "reset_invite_hash", "join_muted", "messages_enabled", "send_paid_messages_stars"]

    ID = 0x974392f2
    QUALNAME = "functions.phone.ToggleGroupCallSettings"

    def __init__(self, *, call: "raw.base.InputGroupCall", reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.reset_invite_hash = reset_invite_hash  # flags.1?true
        self.join_muted = join_muted  # flags.0?Bool
        self.messages_enabled = messages_enabled  # flags.2?Bool
        self.send_paid_messages_stars = send_paid_messages_stars  # flags.3?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallSettings":

        flags = Int.read(b)

        reset_invite_hash = True if flags & (1 << 1) else False
        call = TLObject.read(b)

        join_muted = Bool.read(b) if flags & (1 << 0) else None
        messages_enabled = Bool.read(b) if flags & (1 << 2) else None
        send_paid_messages_stars = Long.read(b) if flags & (1 << 3) else None
        return ToggleGroupCallSettings(call=call, reset_invite_hash=reset_invite_hash, join_muted=join_muted, messages_enabled=messages_enabled, send_paid_messages_stars=send_paid_messages_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.reset_invite_hash else 0
        flags |= (1 << 0) if self.join_muted is not None else 0
        flags |= (1 << 2) if self.messages_enabled is not None else 0
        flags |= (1 << 3) if self.send_paid_messages_stars is not None else 0
        b.write(Int(flags))

        b.write(self.call.write())

        if self.join_muted is not None:
            b.write(Bool(self.join_muted))

        if self.messages_enabled is not None:
            b.write(Bool(self.messages_enabled))

        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))

        return b.getvalue()
