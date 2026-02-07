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


class DeactivateAllUsernames(TLObject):  # type: ignore
    """Disable all purchased usernames of a supergroup or channel


    Details:
        - Layer: ``224``
        - ID: ``A245DD3``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup or channel

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel"]

    ID = 0xa245dd3
    QUALNAME = "functions.channels.DeactivateAllUsernames"

    def __init__(self, *, channel: "raw.base.InputChannel") -> None:
        self.channel = channel  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeactivateAllUsernames":
        # No flags

        channel = TLObject.read(b)

        return DeactivateAllUsernames(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        return b.getvalue()
