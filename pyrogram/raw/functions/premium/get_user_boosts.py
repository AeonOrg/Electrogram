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


class GetUserBoosts(TLObject):  # type: ignore
    """Returns the lists of boost that were applied to a channel by a specific user (admins only)


    Details:
        - Layer: ``224``
        - ID: ``39854D1F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The channel

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The user

    Returns:
        :obj:`premium.BoostsList <pyrogram.raw.base.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "user_id"]

    ID = 0x39854d1f
    QUALNAME = "functions.premium.GetUserBoosts"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser") -> None:
        self.peer = peer  # InputPeer
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserBoosts":
        # No flags

        peer = TLObject.read(b)

        user_id = TLObject.read(b)

        return GetUserBoosts(peer=peer, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.user_id.write())

        return b.getvalue()
