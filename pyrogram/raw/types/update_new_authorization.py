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


class UpdateNewAuthorization(TLObject):  # type: ignore
    """A new session logged into the current user's account through an unknown device.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8951ABEF``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        unconfirmed (``bool``, *optional*):
            Whether the session is unconfirmed, see here » for more info.

        date (``int`` ``32-bit``, *optional*):
            Authorization date

        device (``str``, *optional*):
            Name of device, for example Android

        location (``str``, *optional*):
            Location, for example USA, NY (IP=1.2.3.4)

    """

    __slots__: List[str] = ["hash", "unconfirmed", "date", "device", "location"]

    ID = 0x8951abef
    QUALNAME = "types.UpdateNewAuthorization"

    def __init__(self, *, hash: int, unconfirmed: Optional[bool] = None, date: Optional[int] = None, device: Optional[str] = None, location: Optional[str] = None) -> None:
        self.hash = hash  # long
        self.unconfirmed = unconfirmed  # flags.0?true
        self.date = date  # flags.0?int
        self.device = device  # flags.0?string
        self.location = location  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewAuthorization":

        flags = Int.read(b)

        unconfirmed = True if flags & (1 << 0) else False
        hash = Long.read(b)

        date = Int.read(b) if flags & (1 << 0) else None
        device = String.read(b) if flags & (1 << 0) else None
        location = String.read(b) if flags & (1 << 0) else None
        return UpdateNewAuthorization(hash=hash, unconfirmed=unconfirmed, date=date, device=device, location=location)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unconfirmed else 0
        flags |= (1 << 0) if self.date is not None else 0
        flags |= (1 << 0) if self.device is not None else 0
        flags |= (1 << 0) if self.location is not None else 0
        b.write(Int(flags))

        b.write(Long(self.hash))

        if self.date is not None:
            b.write(Int(self.date))

        if self.device is not None:
            b.write(String(self.device))

        if self.location is not None:
            b.write(String(self.location))

        return b.getvalue()
