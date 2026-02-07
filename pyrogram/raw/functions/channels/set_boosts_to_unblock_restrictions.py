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


class SetBoostsToUnblockRestrictions(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``AD399CEE``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):


        boosts (``int`` ``32-bit``):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "boosts"]

    ID = 0xad399cee
    QUALNAME = "functions.channels.SetBoostsToUnblockRestrictions"

    def __init__(self, *, channel: "raw.base.InputChannel", boosts: int) -> None:
        self.channel = channel  # InputChannel
        self.boosts = boosts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBoostsToUnblockRestrictions":
        # No flags

        channel = TLObject.read(b)

        boosts = Int.read(b)

        return SetBoostsToUnblockRestrictions(channel=channel, boosts=boosts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Int(self.boosts))

        return b.getvalue()
