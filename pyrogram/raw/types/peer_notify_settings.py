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


class PeerNotifySettings(TLObject):  # type: ignore
    """Notification settings.

    Constructor of :obj:`~pyrogram.raw.base.PeerNotifySettings`.

    Details:
        - Layer: ``224``
        - ID: ``99622C0C``

    Parameters:
        show_previews (``bool``, *optional*):
            (Ternary value) If set, indicates whether or not to display previews of messages in notifications; otherwise the default behavior should be used.

        silent (``bool``, *optional*):
            (Ternary value) If set, indicates whether to mute or unmute the peer; otherwise the default behavior should be used.

        mute_until (``int`` ``32-bit``, *optional*):
            Mute all notifications until this date

        ios_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Notification sound for the official iOS application

        android_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Notification sound for the official android application

        other_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Notification sound for other applications

        stories_muted (``bool``, *optional*):
            Whether story notifications should be disabled.

        stories_hide_sender (``bool``, *optional*):
            Whether the sender name should be displayed in story notifications.

        stories_ios_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Sound for story notifications on the official iOS application

        stories_android_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Sound for story notifications on the official Android application

        stories_other_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            Sound for story notifications on other applications

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetNotifySettings
    """

    __slots__: List[str] = ["show_previews", "silent", "mute_until", "ios_sound", "android_sound", "other_sound", "stories_muted", "stories_hide_sender", "stories_ios_sound", "stories_android_sound", "stories_other_sound"]

    ID = 0x99622c0c
    QUALNAME = "types.PeerNotifySettings"

    def __init__(self, *, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[int] = None, ios_sound: "raw.base.NotificationSound" = None, android_sound: "raw.base.NotificationSound" = None, other_sound: "raw.base.NotificationSound" = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_ios_sound: "raw.base.NotificationSound" = None, stories_android_sound: "raw.base.NotificationSound" = None, stories_other_sound: "raw.base.NotificationSound" = None) -> None:
        self.show_previews = show_previews  # flags.0?Bool
        self.silent = silent  # flags.1?Bool
        self.mute_until = mute_until  # flags.2?int
        self.ios_sound = ios_sound  # flags.3?NotificationSound
        self.android_sound = android_sound  # flags.4?NotificationSound
        self.other_sound = other_sound  # flags.5?NotificationSound
        self.stories_muted = stories_muted  # flags.6?Bool
        self.stories_hide_sender = stories_hide_sender  # flags.7?Bool
        self.stories_ios_sound = stories_ios_sound  # flags.8?NotificationSound
        self.stories_android_sound = stories_android_sound  # flags.9?NotificationSound
        self.stories_other_sound = stories_other_sound  # flags.10?NotificationSound

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerNotifySettings":

        flags = Int.read(b)

        show_previews = Bool.read(b) if flags & (1 << 0) else None
        silent = Bool.read(b) if flags & (1 << 1) else None
        mute_until = Int.read(b) if flags & (1 << 2) else None
        ios_sound = TLObject.read(b) if flags & (1 << 3) else None

        android_sound = TLObject.read(b) if flags & (1 << 4) else None

        other_sound = TLObject.read(b) if flags & (1 << 5) else None

        stories_muted = Bool.read(b) if flags & (1 << 6) else None
        stories_hide_sender = Bool.read(b) if flags & (1 << 7) else None
        stories_ios_sound = TLObject.read(b) if flags & (1 << 8) else None

        stories_android_sound = TLObject.read(b) if flags & (1 << 9) else None

        stories_other_sound = TLObject.read(b) if flags & (1 << 10) else None

        return PeerNotifySettings(show_previews=show_previews, silent=silent, mute_until=mute_until, ios_sound=ios_sound, android_sound=android_sound, other_sound=other_sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_ios_sound=stories_ios_sound, stories_android_sound=stories_android_sound, stories_other_sound=stories_other_sound)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.show_previews is not None else 0
        flags |= (1 << 1) if self.silent is not None else 0
        flags |= (1 << 2) if self.mute_until is not None else 0
        flags |= (1 << 3) if self.ios_sound is not None else 0
        flags |= (1 << 4) if self.android_sound is not None else 0
        flags |= (1 << 5) if self.other_sound is not None else 0
        flags |= (1 << 6) if self.stories_muted is not None else 0
        flags |= (1 << 7) if self.stories_hide_sender is not None else 0
        flags |= (1 << 8) if self.stories_ios_sound is not None else 0
        flags |= (1 << 9) if self.stories_android_sound is not None else 0
        flags |= (1 << 10) if self.stories_other_sound is not None else 0
        b.write(Int(flags))

        if self.show_previews is not None:
            b.write(Bool(self.show_previews))

        if self.silent is not None:
            b.write(Bool(self.silent))

        if self.mute_until is not None:
            b.write(Int(self.mute_until))

        if self.ios_sound is not None:
            b.write(self.ios_sound.write())

        if self.android_sound is not None:
            b.write(self.android_sound.write())

        if self.other_sound is not None:
            b.write(self.other_sound.write())

        if self.stories_muted is not None:
            b.write(Bool(self.stories_muted))

        if self.stories_hide_sender is not None:
            b.write(Bool(self.stories_hide_sender))

        if self.stories_ios_sound is not None:
            b.write(self.stories_ios_sound.write())

        if self.stories_android_sound is not None:
            b.write(self.stories_android_sound.write())

        if self.stories_other_sound is not None:
            b.write(self.stories_other_sound.write())

        return b.getvalue()
