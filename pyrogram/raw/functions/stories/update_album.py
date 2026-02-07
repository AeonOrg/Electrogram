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


class UpdateAlbum(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5E5259B6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        album_id (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        delete_stories (List of ``int`` ``32-bit``, *optional*):
            N/A

        add_stories (List of ``int`` ``32-bit``, *optional*):
            N/A

        order (List of ``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`StoryAlbum <pyrogram.raw.base.StoryAlbum>`
    """

    __slots__: List[str] = ["peer", "album_id", "title", "delete_stories", "add_stories", "order"]

    ID = 0x5e5259b6
    QUALNAME = "functions.stories.UpdateAlbum"

    def __init__(self, *, peer: "raw.base.InputPeer", album_id: int, title: Optional[str] = None, delete_stories: Optional[List[int]] = None, add_stories: Optional[List[int]] = None, order: Optional[List[int]] = None) -> None:
        self.peer = peer  # InputPeer
        self.album_id = album_id  # int
        self.title = title  # flags.0?string
        self.delete_stories = delete_stories  # flags.1?Vector<int>
        self.add_stories = add_stories  # flags.2?Vector<int>
        self.order = order  # flags.3?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateAlbum":

        flags = Int.read(b)

        peer = TLObject.read(b)

        album_id = Int.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        delete_stories = TLObject.read(b, Int) if flags & (1 << 1) else []

        add_stories = TLObject.read(b, Int) if flags & (1 << 2) else []

        order = TLObject.read(b, Int) if flags & (1 << 3) else []

        return UpdateAlbum(peer=peer, album_id=album_id, title=title, delete_stories=delete_stories, add_stories=add_stories, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.delete_stories else 0
        flags |= (1 << 2) if self.add_stories else 0
        flags |= (1 << 3) if self.order else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.album_id))

        if self.title is not None:
            b.write(String(self.title))

        if self.delete_stories is not None:
            b.write(Vector(self.delete_stories, Int))

        if self.add_stories is not None:
            b.write(Vector(self.add_stories, Int))

        if self.order is not None:
            b.write(Vector(self.order, Int))

        return b.getvalue()
