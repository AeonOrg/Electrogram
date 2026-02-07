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


class UpdateBotShippingQuery(TLObject):  # type: ignore
    """This object contains information about an incoming shipping query.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B5AEFD7D``

    Parameters:
        query_id (``int`` ``64-bit``):
            Unique query identifier

        user_id (``int`` ``64-bit``):
            User who sent the query

        payload (``bytes``):
            Bot specified invoice payload

        shipping_address (:obj:`PostAddress <pyrogram.raw.base.PostAddress>`):
            User specified shipping address

    """

    __slots__: List[str] = ["query_id", "user_id", "payload", "shipping_address"]

    ID = 0xb5aefd7d
    QUALNAME = "types.UpdateBotShippingQuery"

    def __init__(self, *, query_id: int, user_id: int, payload: bytes, shipping_address: "raw.base.PostAddress") -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # long
        self.payload = payload  # bytes
        self.shipping_address = shipping_address  # PostAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotShippingQuery":
        # No flags

        query_id = Long.read(b)

        user_id = Long.read(b)

        payload = Bytes.read(b)

        shipping_address = TLObject.read(b)

        return UpdateBotShippingQuery(query_id=query_id, user_id=user_id, payload=payload, shipping_address=shipping_address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        b.write(Long(self.user_id))

        b.write(Bytes(self.payload))

        b.write(self.shipping_address.write())

        return b.getvalue()
