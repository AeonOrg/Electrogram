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


class UpdateReadChannelOutbox(TLObject):  # type: ignore
    """Outgoing messages in a channel/supergroup were read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``B75F99A9``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel/supergroup ID

        max_id (``int`` ``32-bit``):
            Position up to which all outgoing messages are read.

    """

    __slots__: List[str] = ["channel_id", "max_id"]

    ID = 0xb75f99a9
    QUALNAME = "types.UpdateReadChannelOutbox"

    def __init__(self, *, channel_id: int, max_id: int) -> None:
        self.channel_id = channel_id  # long
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelOutbox":
        # No flags

        channel_id = Long.read(b)

        max_id = Int.read(b)

        return UpdateReadChannelOutbox(channel_id=channel_id, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Int(self.max_id))

        return b.getvalue()
