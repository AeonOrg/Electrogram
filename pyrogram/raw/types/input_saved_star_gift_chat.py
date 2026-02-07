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


class InputSavedStarGiftChat(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputSavedStarGift`.

    Details:
        - Layer: ``224``
        - ID: ``F101AA7F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        saved_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "saved_id"]

    ID = 0xf101aa7f
    QUALNAME = "types.InputSavedStarGiftChat"

    def __init__(self, *, peer: "raw.base.InputPeer", saved_id: int) -> None:
        self.peer = peer  # InputPeer
        self.saved_id = saved_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSavedStarGiftChat":
        # No flags

        peer = TLObject.read(b)

        saved_id = Long.read(b)

        return InputSavedStarGiftChat(peer=peer, saved_id=saved_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Long(self.saved_id))

        return b.getvalue()
