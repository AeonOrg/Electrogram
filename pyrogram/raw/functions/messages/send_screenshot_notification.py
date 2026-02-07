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


class SendScreenshotNotification(TLObject):  # type: ignore
    """Notify the other user in a private chat that a screenshot of the chat was taken


    Details:
        - Layer: ``224``
        - ID: ``A1405817``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Other user

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`):
            Indicates the message that was screenshotted (the specified message ID can also be 0 to avoid indicating any specific message).

        random_id (``int`` ``64-bit``):
            Random ID to avoid message resending

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "reply_to", "random_id"]

    ID = 0xa1405817
    QUALNAME = "functions.messages.SendScreenshotNotification"

    def __init__(self, *, peer: "raw.base.InputPeer", reply_to: "raw.base.InputReplyTo", random_id: int) -> None:
        self.peer = peer  # InputPeer
        self.reply_to = reply_to  # InputReplyTo
        self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendScreenshotNotification":
        # No flags

        peer = TLObject.read(b)

        reply_to = TLObject.read(b)

        random_id = Long.read(b)

        return SendScreenshotNotification(peer=peer, reply_to=reply_to, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.reply_to.write())

        b.write(Long(self.random_id))

        return b.getvalue()
