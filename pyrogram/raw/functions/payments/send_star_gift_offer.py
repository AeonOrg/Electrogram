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


class SendStarGiftOffer(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8FB86B41``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        slug (``str``):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        duration (``int`` ``32-bit``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "slug", "price", "duration", "random_id", "allow_paid_stars"]

    ID = 0x8fb86b41
    QUALNAME = "functions.payments.SendStarGiftOffer"

    def __init__(self, *, peer: "raw.base.InputPeer", slug: str, price: "raw.base.StarsAmount", duration: int, random_id: int, allow_paid_stars: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.slug = slug  # string
        self.price = price  # StarsAmount
        self.duration = duration  # int
        self.random_id = random_id  # long
        self.allow_paid_stars = allow_paid_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStarGiftOffer":

        flags = Int.read(b)

        peer = TLObject.read(b)

        slug = String.read(b)

        price = TLObject.read(b)

        duration = Int.read(b)

        random_id = Long.read(b)

        allow_paid_stars = Long.read(b) if flags & (1 << 0) else None
        return SendStarGiftOffer(peer=peer, slug=slug, price=price, duration=duration, random_id=random_id, allow_paid_stars=allow_paid_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_paid_stars is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.slug))

        b.write(self.price.write())

        b.write(Int(self.duration))

        b.write(Long(self.random_id))

        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))

        return b.getvalue()
