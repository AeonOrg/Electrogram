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


class AutoSaveException(TLObject):  # type: ignore
    """Peer-specific media autosave settings

    Constructor of :obj:`~pyrogram.raw.base.AutoSaveException`.

    Details:
        - Layer: ``224``
        - ID: ``81602D47``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer

        settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            Media autosave settings

    """

    __slots__: List[str] = ["peer", "settings"]

    ID = 0x81602d47
    QUALNAME = "types.AutoSaveException"

    def __init__(self, *, peer: "raw.base.Peer", settings: "raw.base.AutoSaveSettings") -> None:
        self.peer = peer  # Peer
        self.settings = settings  # AutoSaveSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveException":
        # No flags

        peer = TLObject.read(b)

        settings = TLObject.read(b)

        return AutoSaveException(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.settings.write())

        return b.getvalue()
