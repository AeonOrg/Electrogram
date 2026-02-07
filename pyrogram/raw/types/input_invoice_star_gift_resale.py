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


class InputInvoiceStarGiftResale(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``C39F5324``

    Parameters:
        slug (``str``):
            N/A

        to_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        ton (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["slug", "to_id", "ton"]

    ID = 0xc39f5324
    QUALNAME = "types.InputInvoiceStarGiftResale"

    def __init__(self, *, slug: str, to_id: "raw.base.InputPeer", ton: Optional[bool] = None) -> None:
        self.slug = slug  # string
        self.to_id = to_id  # InputPeer
        self.ton = ton  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftResale":

        flags = Int.read(b)

        ton = True if flags & (1 << 0) else False
        slug = String.read(b)

        to_id = TLObject.read(b)

        return InputInvoiceStarGiftResale(slug=slug, to_id=to_id, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        b.write(Int(flags))

        b.write(String(self.slug))

        b.write(self.to_id.write())

        return b.getvalue()
