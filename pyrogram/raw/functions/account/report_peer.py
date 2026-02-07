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


class ReportPeer(TLObject):  # type: ignore
    """Report a peer for violation of telegram's Terms of Service


    Details:
        - Layer: ``224``
        - ID: ``C5BA3D86``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer to report

        reason (:obj:`ReportReason <pyrogram.raw.base.ReportReason>`):
            The reason why this peer is being reported

        message (``str``):
            Comment for report moderation

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "reason", "message"]

    ID = 0xc5ba3d86
    QUALNAME = "functions.account.ReportPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", reason: "raw.base.ReportReason", message: str) -> None:
        self.peer = peer  # InputPeer
        self.reason = reason  # ReportReason
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportPeer":
        # No flags

        peer = TLObject.read(b)

        reason = TLObject.read(b)

        message = String.read(b)

        return ReportPeer(peer=peer, reason=reason, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.reason.write())

        b.write(String(self.message))

        return b.getvalue()
