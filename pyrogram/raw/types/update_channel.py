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


class UpdateChannel(TLObject):  # type: ignore
    """A new channel or supergroup is available, or info about an existing channel has changed and must be refeteched.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``635B4C09``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

    """

    __slots__: List[str] = ["channel_id"]

    ID = 0x635b4c09
    QUALNAME = "types.UpdateChannel"

    def __init__(self, *, channel_id: int) -> None:
        self.channel_id = channel_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannel":
        # No flags

        channel_id = Long.read(b)

        return UpdateChannel(channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        return b.getvalue()
