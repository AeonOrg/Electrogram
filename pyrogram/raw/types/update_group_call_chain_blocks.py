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


class UpdateGroupCallChainBlocks(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``A477288F``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        sub_chain_id (``int`` ``32-bit``):
            N/A

        blocks (List of ``bytes``):
            N/A

        next_offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["call", "sub_chain_id", "blocks", "next_offset"]

    ID = 0xa477288f
    QUALNAME = "types.UpdateGroupCallChainBlocks"

    def __init__(self, *, call: "raw.base.InputGroupCall", sub_chain_id: int, blocks: List[bytes], next_offset: int) -> None:
        self.call = call  # InputGroupCall
        self.sub_chain_id = sub_chain_id  # int
        self.blocks = blocks  # Vector<bytes>
        self.next_offset = next_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallChainBlocks":
        # No flags

        call = TLObject.read(b)

        sub_chain_id = Int.read(b)

        blocks = TLObject.read(b, Bytes)

        next_offset = Int.read(b)

        return UpdateGroupCallChainBlocks(call=call, sub_chain_id=sub_chain_id, blocks=blocks, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Int(self.sub_chain_id))

        b.write(Vector(self.blocks, Bytes))

        b.write(Int(self.next_offset))

        return b.getvalue()
