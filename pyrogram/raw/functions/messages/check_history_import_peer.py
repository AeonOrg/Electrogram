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


class CheckHistoryImportPeer(TLObject):  # type: ignore
    """Check whether chat history exported from another chat app can be imported into a specific Telegram chat, click here for more info ».


    Details:
        - Layer: ``224``
        - ID: ``5DC60F03``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat where we want to import history ».

    Returns:
        :obj:`messages.CheckedHistoryImportPeer <pyrogram.raw.base.messages.CheckedHistoryImportPeer>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x5dc60f03
    QUALNAME = "functions.messages.CheckHistoryImportPeer"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckHistoryImportPeer":
        # No flags

        peer = TLObject.read(b)

        return CheckHistoryImportPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
