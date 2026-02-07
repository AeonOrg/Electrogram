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


class GetChannelRecommendations(TLObject):  # type: ignore
    """Obtain a list of similarly themed public channels, selected based on similarities in their subscriber bases.


    Details:
        - Layer: ``224``
        - ID: ``25A71742``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`, *optional*):
            The method will return channels related to the passed channel.

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["channel"]

    ID = 0x25a71742
    QUALNAME = "functions.channels.GetChannelRecommendations"

    def __init__(self, *, channel: "raw.base.InputChannel" = None) -> None:
        self.channel = channel  # flags.0?InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelRecommendations":

        flags = Int.read(b)

        channel = TLObject.read(b) if flags & (1 << 0) else None

        return GetChannelRecommendations(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.channel is not None else 0
        b.write(Int(flags))

        if self.channel is not None:
            b.write(self.channel.write())

        return b.getvalue()
