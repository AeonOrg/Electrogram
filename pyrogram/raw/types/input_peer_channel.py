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


class InputPeerChannel(TLObject):  # type: ignore
    """Defines a channel for further interaction.

    Constructor of :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``224``
        - ID: ``27BCBBFC``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel identifier

        access_hash (``int`` ``64-bit``):
            access_hash value from the channel constructor

    """

    __slots__: List[str] = ["channel_id", "access_hash"]

    ID = 0x27bcbbfc
    QUALNAME = "types.InputPeerChannel"

    def __init__(self, *, channel_id: int, access_hash: int) -> None:
        self.channel_id = channel_id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerChannel":
        # No flags

        channel_id = Long.read(b)

        access_hash = Long.read(b)

        return InputPeerChannel(channel_id=channel_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Long(self.access_hash))

        return b.getvalue()
