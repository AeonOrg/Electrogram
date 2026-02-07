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


class UploadImportedMedia(TLObject):  # type: ignore
    """Upload a media file associated with an imported chat, click here for more info ».


    Details:
        - Layer: ``224``
        - ID: ``2A862092``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The Telegram chat where the media will be imported

        import_id (``int`` ``64-bit``):
            Identifier of a history import session, returned by messages.initHistoryImport

        file_name (``str``):
            File name

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            Media metadata

    Returns:
        :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "import_id", "file_name", "media"]

    ID = 0x2a862092
    QUALNAME = "functions.messages.UploadImportedMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int, file_name: str, media: "raw.base.InputMedia") -> None:
        self.peer = peer  # InputPeer
        self.import_id = import_id  # long
        self.file_name = file_name  # string
        self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadImportedMedia":
        # No flags

        peer = TLObject.read(b)

        import_id = Long.read(b)

        file_name = String.read(b)

        media = TLObject.read(b)

        return UploadImportedMedia(peer=peer, import_id=import_id, file_name=file_name, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Long(self.import_id))

        b.write(String(self.file_name))

        b.write(self.media.write())

        return b.getvalue()
