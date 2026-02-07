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


class ViewSponsoredMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``269E3643``

    Parameters:
        random_id (``bytes``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["random_id"]

    ID = 0x269e3643
    QUALNAME = "functions.messages.ViewSponsoredMessage"

    def __init__(self, *, random_id: bytes) -> None:
        self.random_id = random_id  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ViewSponsoredMessage":
        # No flags

        random_id = Bytes.read(b)

        return ViewSponsoredMessage(random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.random_id))

        return b.getvalue()
