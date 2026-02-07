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


class ToggleNoForwards(TLObject):  # type: ignore
    """Enable or disable content protection on a channel or chat


    Details:
        - Layer: ``224``
        - ID: ``B11EAFA2``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat or channel

        enabled (``bool``):
            Enable or disable content protection

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "enabled"]

    ID = 0xb11eafa2
    QUALNAME = "functions.messages.ToggleNoForwards"

    def __init__(self, *, peer: "raw.base.InputPeer", enabled: bool) -> None:
        self.peer = peer  # InputPeer
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleNoForwards":
        # No flags

        peer = TLObject.read(b)

        enabled = Bool.read(b)

        return ToggleNoForwards(peer=peer, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
