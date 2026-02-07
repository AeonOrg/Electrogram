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


class ReceivedCall(TLObject):  # type: ignore
    """Optional: notify the server that the user is currently busy in a call: this will automatically refuse all incoming phone calls until the current phone call is ended.


    Details:
        - Layer: ``224``
        - ID: ``17D54F61``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            The phone call we're currently in

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x17d54f61
    QUALNAME = "functions.phone.ReceivedCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall") -> None:
        self.peer = peer  # InputPhoneCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedCall":
        # No flags

        peer = TLObject.read(b)

        return ReceivedCall(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
