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


class GetNotifySettings(TLObject):  # type: ignore
    """Gets current notification settings for a given user/group, from all users/all groups.


    Details:
        - Layer: ``224``
        - ID: ``12B3AD31``

    Parameters:
        peer (:obj:`InputNotifyPeer <pyrogram.raw.base.InputNotifyPeer>`):
            Notification source

    Returns:
        :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x12b3ad31
    QUALNAME = "functions.account.GetNotifySettings"

    def __init__(self, *, peer: "raw.base.InputNotifyPeer") -> None:
        self.peer = peer  # InputNotifyPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNotifySettings":
        # No flags

        peer = TLObject.read(b)

        return GetNotifySettings(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
