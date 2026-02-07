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


class InvokeWithReCaptcha(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ADBB0F94``

    Parameters:
        token (``str``):
            N/A

        query (Any function from :obj:`~pyrogram.raw.functions`):
            N/A

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["token", "query"]

    ID = 0xadbb0f94
    QUALNAME = "functions.InvokeWithReCaptcha"

    def __init__(self, *, token: str, query: TLObject) -> None:
        self.token = token  # string
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithReCaptcha":
        # No flags

        token = String.read(b)

        query = TLObject.read(b)

        return InvokeWithReCaptcha(token=token, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.token))

        b.write(self.query.write())

        return b.getvalue()
