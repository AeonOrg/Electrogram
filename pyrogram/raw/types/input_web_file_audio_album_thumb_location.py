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


class InputWebFileAudioAlbumThumbLocation(TLObject):  # type: ignore
    """Used to download an album cover for any music file using upload.getWebFile, see the webfile docs for more info ».

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``F46FE924``

    Parameters:
        small (``bool``, *optional*):
            Used to return a thumbnail with 100x100 resolution (instead of the default 600x600)

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            The audio file in question: must NOT be provided in secret chats, provide the title and performer fields instead.

        title (``str``, *optional*):
            Song title: should only be used in secret chats, in normal chats provide document instead, as it has more lax rate limits.

        performer (``str``, *optional*):
            Song performer: should only be used in secret chats, in normal chats provide document instead, as it has more lax rate limits.

    """

    __slots__: List[str] = ["small", "document", "title", "performer"]

    ID = 0xf46fe924
    QUALNAME = "types.InputWebFileAudioAlbumThumbLocation"

    def __init__(self, *, small: Optional[bool] = None, document: "raw.base.InputDocument" = None, title: Optional[str] = None, performer: Optional[str] = None) -> None:
        self.small = small  # flags.2?true
        self.document = document  # flags.0?InputDocument
        self.title = title  # flags.1?string
        self.performer = performer  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileAudioAlbumThumbLocation":

        flags = Int.read(b)

        small = True if flags & (1 << 2) else False
        document = TLObject.read(b) if flags & (1 << 0) else None

        title = String.read(b) if flags & (1 << 1) else None
        performer = String.read(b) if flags & (1 << 1) else None
        return InputWebFileAudioAlbumThumbLocation(small=small, document=document, title=title, performer=performer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.small else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        b.write(Int(flags))

        if self.document is not None:
            b.write(self.document.write())

        if self.title is not None:
            b.write(String(self.title))

        if self.performer is not None:
            b.write(String(self.performer))

        return b.getvalue()
