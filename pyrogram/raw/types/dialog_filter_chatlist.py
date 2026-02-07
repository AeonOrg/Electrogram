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


class DialogFilterChatlist(TLObject):  # type: ignore
    """A folder imported using a chat folder deep link ».

    Constructor of :obj:`~pyrogram.raw.base.DialogFilter`.

    Details:
        - Layer: ``224``
        - ID: ``96537BD7``

    Parameters:
        id (``int`` ``32-bit``):
            ID of the folder

        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            Name of the folder (max 12 UTF-8 chars)

        pinned_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Pinned chats, folders can have unlimited pinned chats

        include_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chats to include in the folder

        has_my_invites (``bool``, *optional*):
            Whether the current user has created some chat folder deep links » to share the folder as well.

        title_noanimate (``bool``, *optional*):
            N/A

        emoticon (``str``, *optional*):
            Emoji to use as icon for the folder.

        color (``int`` ``32-bit``, *optional*):


    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "has_my_invites", "title_noanimate", "emoticon", "color"]

    ID = 0x96537bd7
    QUALNAME = "types.DialogFilterChatlist"

    def __init__(self, *, id: int, title: "raw.base.TextWithEntities", pinned_peers: List["raw.base.InputPeer"], include_peers: List["raw.base.InputPeer"], has_my_invites: Optional[bool] = None, title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None) -> None:
        self.id = id  # int
        self.title = title  # TextWithEntities
        self.pinned_peers = pinned_peers  # Vector<InputPeer>
        self.include_peers = include_peers  # Vector<InputPeer>
        self.has_my_invites = has_my_invites  # flags.26?true
        self.title_noanimate = title_noanimate  # flags.28?true
        self.emoticon = emoticon  # flags.25?string
        self.color = color  # flags.27?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilterChatlist":

        flags = Int.read(b)

        has_my_invites = True if flags & (1 << 26) else False
        title_noanimate = True if flags & (1 << 28) else False
        id = Int.read(b)

        title = TLObject.read(b)

        emoticon = String.read(b) if flags & (1 << 25) else None
        color = Int.read(b) if flags & (1 << 27) else None
        pinned_peers = TLObject.read(b)

        include_peers = TLObject.read(b)

        return DialogFilterChatlist(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, has_my_invites=has_my_invites, title_noanimate=title_noanimate, emoticon=emoticon, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 26) if self.has_my_invites else 0
        flags |= (1 << 28) if self.title_noanimate else 0
        flags |= (1 << 25) if self.emoticon is not None else 0
        flags |= (1 << 27) if self.color is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(self.title.write())

        if self.emoticon is not None:
            b.write(String(self.emoticon))

        if self.color is not None:
            b.write(Int(self.color))

        b.write(Vector(self.pinned_peers))

        b.write(Vector(self.include_peers))

        return b.getvalue()
