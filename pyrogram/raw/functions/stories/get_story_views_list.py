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


class GetStoryViewsList(TLObject):  # type: ignore
    """Obtain the list of users that have viewed a specific story we posted


    Details:
        - Layer: ``224``
        - ID: ``7ED23C57``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the story was posted

        id (``int`` ``32-bit``):
            Story ID

        offset (``str``):
            Offset for pagination, obtained from stories.storyViewsList.next_offset

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        just_contacts (``bool``, *optional*):
            Whether to only fetch view reaction/views made by our contacts

        reactions_first (``bool``, *optional*):
            Whether to return storyView info about users that reacted to the story (i.e. if set, the server will first sort results by view date as usual, and then also additionally sort the list by putting storyViews with an associated reaction first in the list). Ignored if forwards_first is set.

        forwards_first (``bool``, *optional*):
            If set, returns forwards and reposts first, then reactions, then other views; otherwise returns interactions sorted just by interaction date.

        q (``str``, *optional*):
            Search for specific peers

    Returns:
        :obj:`stories.StoryViewsList <pyrogram.raw.base.stories.StoryViewsList>`
    """

    __slots__: List[str] = ["peer", "id", "offset", "limit", "just_contacts", "reactions_first", "forwards_first", "q"]

    ID = 0x7ed23c57
    QUALNAME = "functions.stories.GetStoryViewsList"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, offset: str, limit: int, just_contacts: Optional[bool] = None, reactions_first: Optional[bool] = None, forwards_first: Optional[bool] = None, q: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.offset = offset  # string
        self.limit = limit  # int
        self.just_contacts = just_contacts  # flags.0?true
        self.reactions_first = reactions_first  # flags.2?true
        self.forwards_first = forwards_first  # flags.3?true
        self.q = q  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryViewsList":

        flags = Int.read(b)

        just_contacts = True if flags & (1 << 0) else False
        reactions_first = True if flags & (1 << 2) else False
        forwards_first = True if flags & (1 << 3) else False
        peer = TLObject.read(b)

        q = String.read(b) if flags & (1 << 1) else None
        id = Int.read(b)

        offset = String.read(b)

        limit = Int.read(b)

        return GetStoryViewsList(peer=peer, id=id, offset=offset, limit=limit, just_contacts=just_contacts, reactions_first=reactions_first, forwards_first=forwards_first, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.just_contacts else 0
        flags |= (1 << 2) if self.reactions_first else 0
        flags |= (1 << 3) if self.forwards_first else 0
        flags |= (1 << 1) if self.q is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.q is not None:
            b.write(String(self.q))

        b.write(Int(self.id))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
