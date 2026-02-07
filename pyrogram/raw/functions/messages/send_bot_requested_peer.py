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


class SendBotRequestedPeer(TLObject):  # type: ignore
    """Send one or more chosen peers, as requested by a keyboardButtonRequestPeer button.


    Details:
        - Layer: ``224``
        - ID: ``91B2D060``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The bot that sent the keyboardButtonRequestPeer button.

        msg_id (``int`` ``32-bit``):
            ID of the message that contained the reply keyboard with the keyboardButtonRequestPeer button.

        button_id (``int`` ``32-bit``):
            The button_id field from the keyboardButtonRequestPeer constructor.

        requested_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chosen peers.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "button_id", "requested_peers"]

    ID = 0x91b2d060
    QUALNAME = "functions.messages.SendBotRequestedPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, button_id: int, requested_peers: List["raw.base.InputPeer"]) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.button_id = button_id  # int
        self.requested_peers = requested_peers  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendBotRequestedPeer":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        button_id = Int.read(b)

        requested_peers = TLObject.read(b)

        return SendBotRequestedPeer(peer=peer, msg_id=msg_id, button_id=button_id, requested_peers=requested_peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Int(self.button_id))

        b.write(Vector(self.requested_peers))

        return b.getvalue()
