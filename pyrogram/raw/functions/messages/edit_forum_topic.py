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


class EditForumTopic(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``CECC1134``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        topic_id (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        closed (``bool``, *optional*):
            N/A

        hidden (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "topic_id", "title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xcecc1134
    QUALNAME = "functions.messages.EditForumTopic"

    def __init__(self, *, peer: "raw.base.InputPeer", topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.topic_id = topic_id  # int
        self.title = title  # flags.0?string
        self.icon_emoji_id = icon_emoji_id  # flags.1?long
        self.closed = closed  # flags.2?Bool
        self.hidden = hidden  # flags.3?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditForumTopic":

        flags = Int.read(b)

        peer = TLObject.read(b)

        topic_id = Int.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return EditForumTopic(peer=peer, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.closed is not None else 0
        flags |= (1 << 3) if self.hidden is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.topic_id))

        if self.title is not None:
            b.write(String(self.title))

        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))

        if self.closed is not None:
            b.write(Bool(self.closed))

        if self.hidden is not None:
            b.write(Bool(self.hidden))

        return b.getvalue()
