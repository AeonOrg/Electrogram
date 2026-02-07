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


class GetBotBusinessConnection(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``76A86270``

    Parameters:
        connection_id (``str``):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["connection_id"]

    ID = 0x76a86270
    QUALNAME = "functions.account.GetBotBusinessConnection"

    def __init__(self, *, connection_id: str) -> None:
        self.connection_id = connection_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotBusinessConnection":
        # No flags

        connection_id = String.read(b)

        return GetBotBusinessConnection(connection_id=connection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.connection_id))

        return b.getvalue()
