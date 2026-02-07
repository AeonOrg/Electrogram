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


class InvokeWithBusinessConnection(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``DD289F8E``

    Parameters:
        connection_id (``str``):


        query (Any function from :obj:`~pyrogram.raw.functions`):


    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["connection_id", "query"]

    ID = 0xdd289f8e
    QUALNAME = "functions.InvokeWithBusinessConnection"

    def __init__(self, *, connection_id: str, query: TLObject) -> None:
        self.connection_id = connection_id  # string
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithBusinessConnection":
        # No flags

        connection_id = String.read(b)

        query = TLObject.read(b)

        return InvokeWithBusinessConnection(connection_id=connection_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.connection_id))

        b.write(self.query.write())

        return b.getvalue()
