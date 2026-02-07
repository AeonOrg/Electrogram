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


class GetGroupCallChainBlocks(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EE9F88A6``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        sub_chain_id (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "sub_chain_id", "offset", "limit"]

    ID = 0xee9f88a6
    QUALNAME = "functions.phone.GetGroupCallChainBlocks"

    def __init__(self, *, call: "raw.base.InputGroupCall", sub_chain_id: int, offset: int, limit: int) -> None:
        self.call = call  # InputGroupCall
        self.sub_chain_id = sub_chain_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallChainBlocks":
        # No flags

        call = TLObject.read(b)

        sub_chain_id = Int.read(b)

        offset = Int.read(b)

        limit = Int.read(b)

        return GetGroupCallChainBlocks(call=call, sub_chain_id=sub_chain_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Int(self.sub_chain_id))

        b.write(Int(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
