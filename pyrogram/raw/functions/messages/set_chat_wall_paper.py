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


class SetChatWallPaper(TLObject):  # type: ignore
    """Set a custom wallpaper » in a specific private chat with another user.


    Details:
        - Layer: ``224``
        - ID: ``8FFACAE1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The private chat where the wallpaper will be set

        for_both (``bool``, *optional*):
            Only for Premium users, sets the specified wallpaper for both users of the chat, without requiring confirmation from the other user.

        revert (``bool``, *optional*):
            If we don't like the new wallpaper the other user of the chat has chosen for us using the for_both flag, we can re-set our previous wallpaper just on our side using this flag.

        wallpaper (:obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`, *optional*):
            The wallpaper », obtained as described in the wallpaper documentation »; must not be provided when installing a wallpaper obtained from a messageActionSetChatWallPaper service message (id must be provided, instead).

        settings (:obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`, *optional*):
            Wallpaper settings, obtained as described in the wallpaper documentation » or from messageActionSetChatWallPaper.wallpaper.settings.

        id (``int`` ``32-bit``, *optional*):
            If the wallpaper was obtained from a messageActionSetChatWallPaper service message, must contain the ID of that message.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "for_both", "revert", "wallpaper", "settings", "id"]

    ID = 0x8ffacae1
    QUALNAME = "functions.messages.SetChatWallPaper"

    def __init__(self, *, peer: "raw.base.InputPeer", for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: "raw.base.InputWallPaper" = None, settings: "raw.base.WallPaperSettings" = None, id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.for_both = for_both  # flags.3?true
        self.revert = revert  # flags.4?true
        self.wallpaper = wallpaper  # flags.0?InputWallPaper
        self.settings = settings  # flags.2?WallPaperSettings
        self.id = id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatWallPaper":

        flags = Int.read(b)

        for_both = True if flags & (1 << 3) else False
        revert = True if flags & (1 << 4) else False
        peer = TLObject.read(b)

        wallpaper = TLObject.read(b) if flags & (1 << 0) else None

        settings = TLObject.read(b) if flags & (1 << 2) else None

        id = Int.read(b) if flags & (1 << 1) else None
        return SetChatWallPaper(peer=peer, for_both=for_both, revert=revert, wallpaper=wallpaper, settings=settings, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.for_both else 0
        flags |= (1 << 4) if self.revert else 0
        flags |= (1 << 0) if self.wallpaper is not None else 0
        flags |= (1 << 2) if self.settings is not None else 0
        flags |= (1 << 1) if self.id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.wallpaper is not None:
            b.write(self.wallpaper.write())

        if self.settings is not None:
            b.write(self.settings.write())

        if self.id is not None:
            b.write(Int(self.id))

        return b.getvalue()
