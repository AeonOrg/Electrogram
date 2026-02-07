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


class SaveDefaultSendAs(TLObject):  # type: ignore
    """Change the default peer that should be used when sending messages, reactions, poll votes to a specific group


    Details:
        - Layer: ``224``
        - ID: ``CCFDDF96``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Group

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The default peer that should be used when sending messages to the group

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "send_as"]

    ID = 0xccfddf96
    QUALNAME = "functions.messages.SaveDefaultSendAs"

    def __init__(self, *, peer: "raw.base.InputPeer", send_as: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer
        self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDefaultSendAs":
        # No flags

        peer = TLObject.read(b)

        send_as = TLObject.read(b)

        return SaveDefaultSendAs(peer=peer, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.send_as.write())

        return b.getvalue()
