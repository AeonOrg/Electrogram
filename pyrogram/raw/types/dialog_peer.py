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


class DialogPeer(TLObject):  # type: ignore
    """Peer

    Constructor of :obj:`~pyrogram.raw.base.DialogPeer`.

    Details:
        - Layer: ``224``
        - ID: ``E56DBF05``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogUnreadMarks
    """

    __slots__: List[str] = ["peer"]

    ID = 0xe56dbf05
    QUALNAME = "types.DialogPeer"

    def __init__(self, *, peer: "raw.base.Peer") -> None:
        self.peer = peer  # Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogPeer":
        # No flags

        peer = TLObject.read(b)

        return DialogPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
