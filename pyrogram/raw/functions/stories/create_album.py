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


class CreateAlbum(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A36396E5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        title (``str``):
            N/A

        stories (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`StoryAlbum <pyrogram.raw.base.StoryAlbum>`
    """

    __slots__: List[str] = ["peer", "title", "stories"]

    ID = 0xa36396e5
    QUALNAME = "functions.stories.CreateAlbum"

    def __init__(self, *, peer: "raw.base.InputPeer", title: str, stories: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.title = title  # string
        self.stories = stories  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateAlbum":
        # No flags

        peer = TLObject.read(b)

        title = String.read(b)

        stories = TLObject.read(b, Int)

        return CreateAlbum(peer=peer, title=title, stories=stories)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(String(self.title))

        b.write(Vector(self.stories, Int))

        return b.getvalue()
