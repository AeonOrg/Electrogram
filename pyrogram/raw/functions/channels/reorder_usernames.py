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


class ReorderUsernames(TLObject):  # type: ignore
    """Reorder active usernames


    Details:
        - Layer: ``224``
        - ID: ``B45CED1D``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            The supergroup or channel

        order (List of ``str``):
            The new order for active usernames. All active usernames must be specified.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "order"]

    ID = 0xb45ced1d
    QUALNAME = "functions.channels.ReorderUsernames"

    def __init__(self, *, channel: "raw.base.InputChannel", order: List[str]) -> None:
        self.channel = channel  # InputChannel
        self.order = order  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderUsernames":
        # No flags

        channel = TLObject.read(b)

        order = TLObject.read(b, String)

        return ReorderUsernames(channel=channel, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Vector(self.order, String))

        return b.getvalue()
