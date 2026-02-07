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


class CreateForumTopic(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2F98C3D5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        title (``str``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        title_missing (``bool``, *optional*):
            N/A

        icon_color (``int`` ``32-bit``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "title", "random_id", "title_missing", "icon_color", "icon_emoji_id", "send_as"]

    ID = 0x2f98c3d5
    QUALNAME = "functions.messages.CreateForumTopic"

    def __init__(self, *, peer: "raw.base.InputPeer", title: str, random_id: int, title_missing: Optional[bool] = None, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.title = title  # string
        self.random_id = random_id  # long
        self.title_missing = title_missing  # flags.4?true
        self.icon_color = icon_color  # flags.0?int
        self.icon_emoji_id = icon_emoji_id  # flags.3?long
        self.send_as = send_as  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateForumTopic":

        flags = Int.read(b)

        title_missing = True if flags & (1 << 4) else False
        peer = TLObject.read(b)

        title = String.read(b)

        icon_color = Int.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 3) else None
        random_id = Long.read(b)

        send_as = TLObject.read(b) if flags & (1 << 2) else None

        return CreateForumTopic(peer=peer, title=title, random_id=random_id, title_missing=title_missing, icon_color=icon_color, icon_emoji_id=icon_emoji_id, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 4) if self.title_missing else 0
        flags |= (1 << 0) if self.icon_color is not None else 0
        flags |= (1 << 3) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.send_as is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.title))

        if self.icon_color is not None:
            b.write(Int(self.icon_color))

        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))

        b.write(Long(self.random_id))

        if self.send_as is not None:
            b.write(self.send_as.write())

        return b.getvalue()
