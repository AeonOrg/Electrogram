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


class AnswerWebhookJSONQuery(TLObject):  # type: ignore
    """Answers a custom query; for bots only


    Details:
        - Layer: ``224``
        - ID: ``E6213F4D``

    Parameters:
        query_id (``int`` ``64-bit``):
            Identifier of a custom query

        data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            JSON-serialized answer to the query

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "data"]

    ID = 0xe6213f4d
    QUALNAME = "functions.bots.AnswerWebhookJSONQuery"

    def __init__(self, *, query_id: int, data: "raw.base.DataJSON") -> None:
        self.query_id = query_id  # long
        self.data = data  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AnswerWebhookJSONQuery":
        # No flags

        query_id = Long.read(b)

        data = TLObject.read(b)

        return AnswerWebhookJSONQuery(query_id=query_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        b.write(self.data.write())

        return b.getvalue()
