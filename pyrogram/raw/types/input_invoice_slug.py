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


class InputInvoiceSlug(TLObject):  # type: ignore
    """An invoice slug taken from an invoice deep link or from the premium_invoice_slug app config parameter »

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``C326CAEF``

    Parameters:
        slug (``str``):
            The invoice slug

    """

    __slots__: List[str] = ["slug"]

    ID = 0xc326caef
    QUALNAME = "types.InputInvoiceSlug"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceSlug":
        # No flags

        slug = String.read(b)

        return InputInvoiceSlug(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
