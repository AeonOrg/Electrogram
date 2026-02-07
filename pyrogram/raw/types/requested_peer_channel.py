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


class RequestedPeerChannel(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.RequestedPeer`.

    Details:
        - Layer: ``224``
        - ID: ``8BA403E4``

    Parameters:
        channel_id (``int`` ``64-bit``):


        title (``str``, *optional*):


        username (``str``, *optional*):


        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):


    """

    __slots__: List[str] = ["channel_id", "title", "username", "photo"]

    ID = 0x8ba403e4
    QUALNAME = "types.RequestedPeerChannel"

    def __init__(self, *, channel_id: int, title: Optional[str] = None, username: Optional[str] = None, photo: "raw.base.Photo" = None) -> None:
        self.channel_id = channel_id  # long
        self.title = title  # flags.0?string
        self.username = username  # flags.1?string
        self.photo = photo  # flags.2?Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerChannel":

        flags = Int.read(b)

        channel_id = Long.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        username = String.read(b) if flags & (1 << 1) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None

        return RequestedPeerChannel(channel_id=channel_id, title=title, username=username, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.username is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))

        b.write(Long(self.channel_id))

        if self.title is not None:
            b.write(String(self.title))

        if self.username is not None:
            b.write(String(self.username))

        if self.photo is not None:
            b.write(self.photo.write())

        return b.getvalue()
