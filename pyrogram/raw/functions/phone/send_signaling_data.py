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


class SendSignalingData(TLObject):  # type: ignore
    """Send VoIP signaling data


    Details:
        - Layer: ``224``
        - ID: ``FF7A9383``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            Phone call

        data (``bytes``):
            Signaling payload

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "data"]

    ID = 0xff7a9383
    QUALNAME = "functions.phone.SendSignalingData"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", data: bytes) -> None:
        self.peer = peer  # InputPhoneCall
        self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendSignalingData":
        # No flags

        peer = TLObject.read(b)

        data = Bytes.read(b)

        return SendSignalingData(peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Bytes(self.data))

        return b.getvalue()
