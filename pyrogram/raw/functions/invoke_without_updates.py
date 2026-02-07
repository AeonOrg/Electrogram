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


class InvokeWithoutUpdates(TLObject):  # type: ignore
    """Invoke a request without subscribing the used connection for updates (this is enabled by default for file queries).


    Details:
        - Layer: ``224``
        - ID: ``BF9459B7``

    Parameters:
        query (Any function from :obj:`~pyrogram.raw.functions`):
            The query

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["query"]

    ID = 0xbf9459b7
    QUALNAME = "functions.InvokeWithoutUpdates"

    def __init__(self, *, query: TLObject) -> None:
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithoutUpdates":
        # No flags

        query = TLObject.read(b)

        return InvokeWithoutUpdates(query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.query.write())

        return b.getvalue()
