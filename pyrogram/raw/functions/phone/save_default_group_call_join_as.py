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


class SaveDefaultGroupCallJoinAs(TLObject):  # type: ignore
    """Set the default peer that will be used to join a group call in a specific dialog.


    Details:
        - Layer: ``224``
        - ID: ``575E1F8C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The dialog

        join_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The default peer that will be used to join group calls in this dialog, presenting yourself as a specific user/channel.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "join_as"]

    ID = 0x575e1f8c
    QUALNAME = "functions.phone.SaveDefaultGroupCallJoinAs"

    def __init__(self, *, peer: "raw.base.InputPeer", join_as: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer
        self.join_as = join_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDefaultGroupCallJoinAs":
        # No flags

        peer = TLObject.read(b)

        join_as = TLObject.read(b)

        return SaveDefaultGroupCallJoinAs(peer=peer, join_as=join_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.join_as.write())

        return b.getvalue()
