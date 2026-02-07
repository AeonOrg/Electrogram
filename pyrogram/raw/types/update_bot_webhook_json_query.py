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


class UpdateBotWebhookJSONQuery(TLObject):  # type: ignore
    """A new incoming query; for bots only

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``9B9240A6``

    Parameters:
        query_id (``int`` ``64-bit``):
            Query identifier

        data (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Query data

        timeout (``int`` ``32-bit``):
            Query timeout

    """

    __slots__: List[str] = ["query_id", "data", "timeout"]

    ID = 0x9b9240a6
    QUALNAME = "types.UpdateBotWebhookJSONQuery"

    def __init__(self, *, query_id: int, data: "raw.base.DataJSON", timeout: int) -> None:
        self.query_id = query_id  # long
        self.data = data  # DataJSON
        self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotWebhookJSONQuery":
        # No flags

        query_id = Long.read(b)

        data = TLObject.read(b)

        timeout = Int.read(b)

        return UpdateBotWebhookJSONQuery(query_id=query_id, data=data, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        b.write(self.data.write())

        b.write(Int(self.timeout))

        return b.getvalue()
