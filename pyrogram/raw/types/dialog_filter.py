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


class DialogFilter(TLObject):  # type: ignore
    """Dialog filter AKA folder

    Constructor of :obj:`~pyrogram.raw.base.DialogFilter`.

    Details:
        - Layer: ``224``
        - ID: ``AA472651``

    Parameters:
        id (``int`` ``32-bit``):
            Folder ID

        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            Folder name (max 12 UTF-8 chars)

        pinned_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Pinned chats, folders can have unlimited pinned chats

        include_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Include the following chats in this folder

        exclude_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Exclude the following chats from this folder

        contacts (``bool``, *optional*):
            Whether to include all contacts in this folder

        non_contacts (``bool``, *optional*):
            Whether to include all non-contacts in this folder

        groups (``bool``, *optional*):
            Whether to include all groups in this folder

        broadcasts (``bool``, *optional*):
            Whether to include all channels in this folder

        bots (``bool``, *optional*):
            Whether to include all bots in this folder

        exclude_muted (``bool``, *optional*):
            Whether to exclude muted chats from this folder

        exclude_read (``bool``, *optional*):
            Whether to exclude read chats from this folder

        exclude_archived (``bool``, *optional*):
            Whether to exclude archived chats from this folder

        title_noanimate (``bool``, *optional*):
            N/A

        emoticon (``str``, *optional*):
            Emoji to use as icon for the folder.

        color (``int`` ``32-bit``, *optional*):


    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "exclude_peers", "contacts", "non_contacts", "groups", "broadcasts", "bots", "exclude_muted", "exclude_read", "exclude_archived", "title_noanimate", "emoticon", "color"]

    ID = 0xaa472651
    QUALNAME = "types.DialogFilter"

    def __init__(self, *, id: int, title: "raw.base.TextWithEntities", pinned_peers: List["raw.base.InputPeer"], include_peers: List["raw.base.InputPeer"], exclude_peers: List["raw.base.InputPeer"], contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, groups: Optional[bool] = None, broadcasts: Optional[bool] = None, bots: Optional[bool] = None, exclude_muted: Optional[bool] = None, exclude_read: Optional[bool] = None, exclude_archived: Optional[bool] = None, title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None) -> None:
        self.id = id  # int
        self.title = title  # TextWithEntities
        self.pinned_peers = pinned_peers  # Vector<InputPeer>
        self.include_peers = include_peers  # Vector<InputPeer>
        self.exclude_peers = exclude_peers  # Vector<InputPeer>
        self.contacts = contacts  # flags.0?true
        self.non_contacts = non_contacts  # flags.1?true
        self.groups = groups  # flags.2?true
        self.broadcasts = broadcasts  # flags.3?true
        self.bots = bots  # flags.4?true
        self.exclude_muted = exclude_muted  # flags.11?true
        self.exclude_read = exclude_read  # flags.12?true
        self.exclude_archived = exclude_archived  # flags.13?true
        self.title_noanimate = title_noanimate  # flags.28?true
        self.emoticon = emoticon  # flags.25?string
        self.color = color  # flags.27?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilter":

        flags = Int.read(b)

        contacts = True if flags & (1 << 0) else False
        non_contacts = True if flags & (1 << 1) else False
        groups = True if flags & (1 << 2) else False
        broadcasts = True if flags & (1 << 3) else False
        bots = True if flags & (1 << 4) else False
        exclude_muted = True if flags & (1 << 11) else False
        exclude_read = True if flags & (1 << 12) else False
        exclude_archived = True if flags & (1 << 13) else False
        title_noanimate = True if flags & (1 << 28) else False
        id = Int.read(b)

        title = TLObject.read(b)

        emoticon = String.read(b) if flags & (1 << 25) else None
        color = Int.read(b) if flags & (1 << 27) else None
        pinned_peers = TLObject.read(b)

        include_peers = TLObject.read(b)

        exclude_peers = TLObject.read(b)

        return DialogFilter(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, exclude_peers=exclude_peers, contacts=contacts, non_contacts=non_contacts, groups=groups, broadcasts=broadcasts, bots=bots, exclude_muted=exclude_muted, exclude_read=exclude_read, exclude_archived=exclude_archived, title_noanimate=title_noanimate, emoticon=emoticon, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.non_contacts else 0
        flags |= (1 << 2) if self.groups else 0
        flags |= (1 << 3) if self.broadcasts else 0
        flags |= (1 << 4) if self.bots else 0
        flags |= (1 << 11) if self.exclude_muted else 0
        flags |= (1 << 12) if self.exclude_read else 0
        flags |= (1 << 13) if self.exclude_archived else 0
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

        b.write(Vector(self.exclude_peers))

        return b.getvalue()
