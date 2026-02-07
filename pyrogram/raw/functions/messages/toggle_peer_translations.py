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


class TogglePeerTranslations(TLObject):  # type: ignore
    """Show or hide the real-time chat translation popup for a certain chat


    Details:
        - Layer: ``224``
        - ID: ``E47CB579``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer

        disabled (``bool``, *optional*):
            Whether to disable or enable the real-time chat translation popup

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "disabled"]

    ID = 0xe47cb579
    QUALNAME = "functions.messages.TogglePeerTranslations"

    def __init__(self, *, peer: "raw.base.InputPeer", disabled: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.disabled = disabled  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePeerTranslations":

        flags = Int.read(b)

        disabled = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        return TogglePeerTranslations(peer=peer, disabled=disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.disabled else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        return b.getvalue()
