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


class InputPeerColorCollectible(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerColor`.

    Details:
        - Layer: ``224``
        - ID: ``B8EA86A9``

    Parameters:
        collectible_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["collectible_id"]

    ID = 0xb8ea86a9
    QUALNAME = "types.InputPeerColorCollectible"

    def __init__(self, *, collectible_id: int) -> None:
        self.collectible_id = collectible_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerColorCollectible":
        # No flags

        collectible_id = Long.read(b)

        return InputPeerColorCollectible(collectible_id=collectible_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.collectible_id))

        return b.getvalue()
