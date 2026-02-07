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


class InvokeWithMessagesRange(TLObject):  # type: ignore
    """Invoke with the given message range


    Details:
        - Layer: ``224``
        - ID: ``365275F2``

    Parameters:
        range (:obj:`MessageRange <pyrogram.raw.base.MessageRange>`):
            Message range

        query (Any function from :obj:`~pyrogram.raw.functions`):
            Query

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["range", "query"]

    ID = 0x365275f2
    QUALNAME = "functions.InvokeWithMessagesRange"

    def __init__(self, *, range: "raw.base.MessageRange", query: TLObject) -> None:
        self.range = range  # MessageRange
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithMessagesRange":
        # No flags

        range = TLObject.read(b)

        query = TLObject.read(b)

        return InvokeWithMessagesRange(range=range, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.range.write())

        b.write(self.query.write())

        return b.getvalue()
