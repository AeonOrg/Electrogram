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


class SaveCallDebug(TLObject):  # type: ignore
    """Send phone call debug data to server


    Details:
        - Layer: ``224``
        - ID: ``277ADD7E``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            Phone call

        debug (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Debug statistics obtained from libtgvoip

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "debug"]

    ID = 0x277add7e
    QUALNAME = "functions.phone.SaveCallDebug"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", debug: "raw.base.DataJSON") -> None:
        self.peer = peer  # InputPhoneCall
        self.debug = debug  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveCallDebug":
        # No flags

        peer = TLObject.read(b)

        debug = TLObject.read(b)

        return SaveCallDebug(peer=peer, debug=debug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.debug.write())

        return b.getvalue()
