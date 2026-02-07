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


class ReportProfilePhoto(TLObject):  # type: ignore
    """Report a profile photo of a dialog


    Details:
        - Layer: ``224``
        - ID: ``FA8CC6F5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The dialog

        photo_id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            Dialog photo ID

        reason (:obj:`ReportReason <pyrogram.raw.base.ReportReason>`):
            Report reason

        message (``str``):
            Comment for report moderation

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "photo_id", "reason", "message"]

    ID = 0xfa8cc6f5
    QUALNAME = "functions.account.ReportProfilePhoto"

    def __init__(self, *, peer: "raw.base.InputPeer", photo_id: "raw.base.InputPhoto", reason: "raw.base.ReportReason", message: str) -> None:
        self.peer = peer  # InputPeer
        self.photo_id = photo_id  # InputPhoto
        self.reason = reason  # ReportReason
        self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportProfilePhoto":
        # No flags

        peer = TLObject.read(b)

        photo_id = TLObject.read(b)

        reason = TLObject.read(b)

        message = String.read(b)

        return ReportProfilePhoto(peer=peer, photo_id=photo_id, reason=reason, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.photo_id.write())

        b.write(self.reason.write())

        b.write(String(self.message))

        return b.getvalue()
