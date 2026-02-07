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


class GetGameHighScores(TLObject):  # type: ignore
    """Get highscores of a game


    Details:
        - Layer: ``224``
        - ID: ``E822649D``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Where was the game sent

        id (``int`` ``32-bit``):
            ID of message with game media attachment

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Get high scores made by a certain user

    Returns:
        :obj:`messages.HighScores <pyrogram.raw.base.messages.HighScores>`
    """

    __slots__: List[str] = ["peer", "id", "user_id"]

    ID = 0xe822649d
    QUALNAME = "functions.messages.GetGameHighScores"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, user_id: "raw.base.InputUser") -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGameHighScores":
        # No flags

        peer = TLObject.read(b)

        id = Int.read(b)

        user_id = TLObject.read(b)

        return GetGameHighScores(peer=peer, id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.id))

        b.write(self.user_id.write())

        return b.getvalue()
