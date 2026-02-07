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


class WebFile(TLObject):  # type: ignore
    """Represents a chunk of an HTTP webfile downloaded through telegram's secure MTProto servers

    Constructor of :obj:`~pyrogram.raw.base.upload.WebFile`.

    Details:
        - Layer: ``224``
        - ID: ``21E753BC``

    Parameters:
        size (``int`` ``32-bit``):
            File size

        mime_type (``str``):
            Mime type

        file_type (:obj:`storage.FileType <pyrogram.raw.base.storage.FileType>`):
            File type

        mtime (``int`` ``32-bit``):
            Modified time

        bytes (``bytes``):
            Data

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetWebFile
    """

    __slots__: List[str] = ["size", "mime_type", "file_type", "mtime", "bytes"]

    ID = 0x21e753bc
    QUALNAME = "types.upload.WebFile"

    def __init__(self, *, size: int, mime_type: str, file_type: "raw.base.storage.FileType", mtime: int, bytes: bytes) -> None:
        self.size = size  # int
        self.mime_type = mime_type  # string
        self.file_type = file_type  # storage.FileType
        self.mtime = mtime  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebFile":
        # No flags

        size = Int.read(b)

        mime_type = String.read(b)

        file_type = TLObject.read(b)

        mtime = Int.read(b)

        bytes = Bytes.read(b)

        return WebFile(size=size, mime_type=mime_type, file_type=file_type, mtime=mtime, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.size))

        b.write(String(self.mime_type))

        b.write(self.file_type.write())

        b.write(Int(self.mtime))

        b.write(Bytes(self.bytes))

        return b.getvalue()
