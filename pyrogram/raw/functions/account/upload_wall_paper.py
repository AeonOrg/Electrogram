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


class UploadWallPaper(TLObject):  # type: ignore
    """Create and upload a new wallpaper


    Details:
        - Layer: ``224``
        - ID: ``E39A8F03``

    Parameters:
        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`):
            The JPG/PNG wallpaper

        mime_type (``str``):
            MIME type of uploaded wallpaper

        settings (:obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`):
            Wallpaper settings

        for_chat (``bool``, *optional*):
            Set this flag when uploading wallpapers to be passed to messages.setChatWallPaper.

    Returns:
        :obj:`WallPaper <pyrogram.raw.base.WallPaper>`
    """

    __slots__: List[str] = ["file", "mime_type", "settings", "for_chat"]

    ID = 0xe39a8f03
    QUALNAME = "functions.account.UploadWallPaper"

    def __init__(self, *, file: "raw.base.InputFile", mime_type: str, settings: "raw.base.WallPaperSettings", for_chat: Optional[bool] = None) -> None:
        self.file = file  # InputFile
        self.mime_type = mime_type  # string
        self.settings = settings  # WallPaperSettings
        self.for_chat = for_chat  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadWallPaper":

        flags = Int.read(b)

        for_chat = True if flags & (1 << 0) else False
        file = TLObject.read(b)

        mime_type = String.read(b)

        settings = TLObject.read(b)

        return UploadWallPaper(file=file, mime_type=mime_type, settings=settings, for_chat=for_chat)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.for_chat else 0
        b.write(Int(flags))

        b.write(self.file.write())

        b.write(String(self.mime_type))

        b.write(self.settings.write())

        return b.getvalue()
