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


class StartHistoryImport(TLObject):  # type: ignore
    """Complete the history import process, importing all messages into the chat.
To be called only after initializing the import with messages.initHistoryImport and uploading all files using messages.uploadImportedMedia.


    Details:
        - Layer: ``224``
        - ID: ``B43DF344``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The Telegram chat where the messages should be imported, click here for more info »

        import_id (``int`` ``64-bit``):
            Identifier of a history import session, returned by messages.initHistoryImport.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "import_id"]

    ID = 0xb43df344
    QUALNAME = "functions.messages.StartHistoryImport"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int) -> None:
        self.peer = peer  # InputPeer
        self.import_id = import_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartHistoryImport":
        # No flags

        peer = TLObject.read(b)

        import_id = Long.read(b)

        return StartHistoryImport(peer=peer, import_id=import_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Long(self.import_id))

        return b.getvalue()
