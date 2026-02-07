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


class InitHistoryImport(TLObject):  # type: ignore
    """Import chat history from a foreign chat app into a specific Telegram chat, click here for more info about imported chats ».


    Details:
        - Layer: ``224``
        - ID: ``34090C3B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The Telegram chat where the history should be imported.

        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`):
            File with messages to import.

        media_count (``int`` ``32-bit``):
            Number of media files associated with the chat that will be uploaded using messages.uploadImportedMedia.

    Returns:
        :obj:`messages.HistoryImport <pyrogram.raw.base.messages.HistoryImport>`
    """

    __slots__: List[str] = ["peer", "file", "media_count"]

    ID = 0x34090c3b
    QUALNAME = "functions.messages.InitHistoryImport"

    def __init__(self, *, peer: "raw.base.InputPeer", file: "raw.base.InputFile", media_count: int) -> None:
        self.peer = peer  # InputPeer
        self.file = file  # InputFile
        self.media_count = media_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitHistoryImport":
        # No flags

        peer = TLObject.read(b)

        file = TLObject.read(b)

        media_count = Int.read(b)

        return InitHistoryImport(peer=peer, file=file, media_count=media_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.file.write())

        b.write(Int(self.media_count))

        return b.getvalue()
