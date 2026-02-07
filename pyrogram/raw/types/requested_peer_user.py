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


class RequestedPeerUser(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.RequestedPeer`.

    Details:
        - Layer: ``224``
        - ID: ``D62FF46A``

    Parameters:
        user_id (``int`` ``64-bit``):


        first_name (``str``, *optional*):


        last_name (``str``, *optional*):


        username (``str``, *optional*):


        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):


    """

    __slots__: List[str] = ["user_id", "first_name", "last_name", "username", "photo"]

    ID = 0xd62ff46a
    QUALNAME = "types.RequestedPeerUser"

    def __init__(self, *, user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, photo: "raw.base.Photo" = None) -> None:
        self.user_id = user_id  # long
        self.first_name = first_name  # flags.0?string
        self.last_name = last_name  # flags.0?string
        self.username = username  # flags.1?string
        self.photo = photo  # flags.2?Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedPeerUser":

        flags = Int.read(b)

        user_id = Long.read(b)

        first_name = String.read(b) if flags & (1 << 0) else None
        last_name = String.read(b) if flags & (1 << 0) else None
        username = String.read(b) if flags & (1 << 1) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None

        return RequestedPeerUser(user_id=user_id, first_name=first_name, last_name=last_name, username=username, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.first_name is not None else 0
        flags |= (1 << 0) if self.last_name is not None else 0
        flags |= (1 << 1) if self.username is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))

        b.write(Long(self.user_id))

        if self.first_name is not None:
            b.write(String(self.first_name))

        if self.last_name is not None:
            b.write(String(self.last_name))

        if self.username is not None:
            b.write(String(self.username))

        if self.photo is not None:
            b.write(self.photo.write())

        return b.getvalue()
