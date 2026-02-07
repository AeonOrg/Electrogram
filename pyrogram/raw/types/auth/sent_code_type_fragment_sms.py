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


class SentCodeTypeFragmentSms(TLObject):  # type: ignore
    """The code was delivered via fragment.com.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``D9565C39``

    Parameters:
        url (``str``):
            Open the specified URL to log into fragment.com with the wallet that owns the specified phone number and view the code.

        length (``int`` ``32-bit``):
            Length of the delivered code.

    """

    __slots__: List[str] = ["url", "length"]

    ID = 0xd9565c39
    QUALNAME = "types.auth.SentCodeTypeFragmentSms"

    def __init__(self, *, url: str, length: int) -> None:
        self.url = url  # string
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFragmentSms":
        # No flags

        url = String.read(b)

        length = Int.read(b)

        return SentCodeTypeFragmentSms(url=url, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Int(self.length))

        return b.getvalue()
